# pylint: disable=missing-docstring
import unittest
from unittest.mock import patch, MagicMock
import os
from soil.finder import Finder


class TestFinder(unittest.TestCase):
    def test_fail_to_find(self) -> None:
        finder = Finder()
        spec = finder.find_spec(fullname="nonvalid.module", path=[])
        assert spec is None

    @patch("soil.finder.spec_from_file_location")
    @patch("soil.finder.os.path.exists")
    def test_find_file(
        self, mock_path_exists: MagicMock, mock_spec_from_file_location: MagicMock
    ) -> None:
        os.environ["MODULES_PATH"] = "myapp/modules"
        os.environ["DATA_STRUCTURES_PATH"] = "myapp/modules"
        mock_spec_from_file_location.return_value = "ok"
        mock_path_exists.return_value = True
        finder = Finder()
        spec = finder.find_spec(fullname="myapp.modules.module", path=[])
        assert spec == "ok"

    @patch("soil.finder.spec_from_file_location")
    @patch("soil.finder.os.path.exists")
    def test_outside_folders(
        self, mock_path_exists: MagicMock, mock_spec_from_file_location: MagicMock
    ) -> None:
        os.environ["MODULES_PATH"] = "myapp/modules"
        os.environ["DATA_STRUCTURES_PATH"] = "myapp/modules"
        mock_spec_from_file_location.return_value = "ok"
        mock_path_exists.return_value = True
        finder = Finder()
        spec = finder.find_spec(fullname="myapp.something.module", path=[])
        assert spec is None

    @patch("soil.finder.spec_from_file_location")
    @patch("soil.finder.os.path.exists")
    def test_import_library(
        self, mock_path_exists: MagicMock, mock_spec_from_file_location: MagicMock
    ) -> None:
        os.environ["MODULES_PATH"] = "myapp/modules"
        os.environ["DATA_STRUCTURES_PATH"] = "myapp/modules"
        mock_spec_from_file_location.return_value = "ok"
        mock_path_exists.return_value = True
        finder = Finder()
        spec = finder.find_spec(fullname="gc", path=[])
        assert spec is None

    @patch("soil.finder.spec_from_file_location")
    @patch("soil.finder.os.path.exists")
    def test_import_outside_app(
        self, mock_path_exists: MagicMock, mock_spec_from_file_location: MagicMock
    ) -> None:
        os.environ["MODULES_PATH"] = "myapp/modules"
        os.environ["DATA_STRUCTURES_PATH"] = "myapp/modules"
        mock_spec_from_file_location.return_value = "ok"
        mock_path_exists.return_value = True
        finder = Finder()
        spec = finder.find_spec(fullname="myfolder.modules.something", path=[])
        assert spec is None

    @patch("soil.finder.spec_from_file_location")
    @patch("soil.finder.os.path.exists")
    def test_import_not_found(
        self, mock_path_exists: MagicMock, mock_spec_from_file_location: MagicMock
    ) -> None:
        os.environ["MODULES_PATH"] = "myapp/modules"
        os.environ["DATA_STRUCTURES_PATH"] = "myapp/modules"
        mock_spec_from_file_location.return_value = "ok"
        mock_path_exists.return_value = False
        finder = Finder()
        spec = finder.find_spec(fullname="myapp.modules.something", path=[])
        assert spec is None

    @patch("soil.finder.spec_from_loader")
    @patch("soil.finder.os.path.exists")
    @patch("soil.api.get_module")
    def test_import_from_db(
        self,
        _mock_get_module: MagicMock,
        mock_path_exists: MagicMock,
        mock_spec_from_loader: MagicMock,
    ) -> None:
        os.environ["MODULES_PATH"] = "myapp/modules"
        os.environ["DATA_STRUCTURES_PATH"] = "myapp/modules"
        mock_spec_from_loader.return_value = "ok"
        mock_path_exists.return_value = False
        finder = Finder()
        spec = finder.find_spec(fullname="soil.modules.something", path=[])
        assert spec == "ok"
