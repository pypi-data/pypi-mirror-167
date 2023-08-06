"""
This module overrides Python's import system
https://docs.python.org/3/library/importlib.html
https://stackoverflow.com/a/43573798/3481480
"""

import os.path

# pylint: disable=unused-argument,abstract-method,exec-used
import sys
import types
from importlib.abc import Loader, MetaPathFinder
from importlib.machinery import ModuleSpec
from importlib.util import spec_from_file_location, spec_from_loader
from typing import List, Optional, Sequence, Union

from soil import api


def _get_app_name() -> Optional[str]:
    modules_path = os.getenv("MODULES_PATH")
    if modules_path is None:
        return None
    return modules_path.split("/")[-2]


def _upload_base_modules() -> None:
    app_name = _get_app_name()
    if app_name is None:
        return
    api.upload_module(module_name=app_name, code="", is_package=True)
    api.upload_module(module_name=f"{app_name}.modules", code="", is_package=True)
    api.upload_module(
        module_name=f"{app_name}.data_structures", code="", is_package=True
    )


if os.environ.get("PY_ENV", "development") != "test":
    _upload_base_modules()


class Finder(MetaPathFinder):
    """
    Custom finder that uploads a module or data_structure to the cloud and if
    the module is not found locally it is downloaded from the cloud
    """

    def find_spec(
        self,
        fullname: str,
        path: Optional[Sequence[Union[bytes, str]]],
        target: Optional[types.ModuleType] = None,
    ) -> Optional[ModuleSpec]:
        """find_spec implementation"""
        can_be_in_db = False
        app_name = _get_app_name()
        if path is None or path == "":
            path = [os.path.abspath(os.path.curdir)]  # top level import --
        if "." in fullname:
            *parents, name = fullname.split(".")
        else:
            name = fullname
            parents = []
        if (
            len(parents) > 1
            and parents[0] in (app_name, "soil")
            and parents[1] in ("modules", "data_structures")
        ):
            path = list(path)
            path += [os.environ["MODULES_PATH"], os.environ["DATA_STRUCTURES_PATH"]]
            can_be_in_db = parents[0] == "soil"
        else:
            # If the module is not from app_name.modules or app_name.data_structures
            # use the default loader
            return None

        for entry in path:
            entry = str(entry)
            if os.path.isdir(os.path.join(entry, name)):
                # this module has child modules
                filename = os.path.join(entry, name, "__init__.py")
                submodule_locations: Optional[List[str]] = [os.path.join(entry, name)]
            else:
                filename = os.path.join(entry, name + ".py")
                submodule_locations = None
            if not os.path.exists(filename):
                continue

            return spec_from_file_location(
                fullname,
                filename,
                loader=CustomLoader(fullname, filename),
                submodule_search_locations=submodule_locations,
            )

        # If the module is not found look for it in the DB
        if can_be_in_db:
            mod = api.get_module(fullname)
            is_package = mod.get("is_package", False)
            code = _generate_code(
                public_api=mod.get("public_api", []),
                package_type=mod.get("package_type", ""),
            )
            if code is not None:
                return spec_from_loader(
                    fullname,
                    loader=CustomLoader(
                        fullname, code=code, from_db=True, is_package=is_package
                    ),
                    is_package=is_package,
                )
        return None  # returning None raises not found error


def _generate_code(public_api: List[str], package_type: str) -> str:
    code = ""
    if package_type == "modules":
        for public_fn in public_api:
            code += (
                f"from soil import modulify\n@modulify(_from_db=True)"
                f"\ndef {public_fn}(*args, **kwargs):\n    pass\n\n"
            )
    if package_type == "data_structures":
        for public_fn in public_api:
            code += f"class {public_fn}:\n    pass\n\n"
    return code


class CustomLoader(Loader):
    """This class runs modules and uploads them"""

    def __init__(
        self,
        fullname: str,
        filename: Optional[str] = None,
        code: Optional[str] = None,
        from_db: bool = False,
        is_package: bool = False,
    ):
        self.filename = filename
        self.fullname = fullname
        self.code = code
        self.from_db = from_db
        self.is_package = is_package

    def create_module(self, spec: ModuleSpec) -> None:
        """Use default module creation semantics"""
        return None

    def exec_module(self, module: types.ModuleType) -> None:
        """Load code if necessary, upload it and run it."""
        is_package = self.is_package
        if self.from_db:
            top_module = "soil"
        else:
            app_name = _get_app_name()
            if app_name is None:
                return
            top_module = app_name
        if self.code is None and self.filename is not None:
            size_init = len("__init__.py")
            is_package = self.filename[-size_init:] == "__init__.py"
            with open(self.filename, encoding="utf-8") as f:
                self.code = f.read()
        if self.code is not None and (
            self.fullname[: len(f"{top_module}.modules")] == f"{top_module}.modules"
            or self.fullname[: len(f"{top_module}.data_structures")]
            == f"{top_module}.data_structures"
        ):
            if not self.from_db and os.environ.get("PY_ENV", "development") != "test":
                api.upload_module(self.fullname, self.code, is_package)
            name = self.filename if self.filename is not None else self.fullname
            compiled_module = compile(self.code, name, "exec")
            exec(compiled_module, vars(module))  # nosec


def install() -> None:
    """Inserts the finder into the import machinery"""
    sys.meta_path.insert(0, Finder())
