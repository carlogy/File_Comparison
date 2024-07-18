from get_file_paths import checkDir, getFilePaths
import pytest

class TestGetFile:
    def test_path_exists_false(self):
        environmentInput = "InvalidPath"
        with pytest.raises(FileNotFoundError):
            checkDir(environmentInput)

    def test_path_exists_true(self):
        environmentInput = "Dev"
        actual = checkDir(environmentInput)
        expected = f"./validationFiles/{environmentInput.lower()}"

        assert actual == expected

    def test_file_paths_children_exist(self):
        environmentInput = "Test"
        actual = getFilePaths(checkDir(environmentInput))
        expected = ['./validationFiles/test/test1.json', './validationFiles/test/test3.csv', './validationFiles/test/test2.json']
        assert actual == expected

    def test_file_paths_no_children(self):
        environmentInput = "Staging"
        actual = getFilePaths(checkDir(environmentInput))
        expected = []
        assert actual == expected
