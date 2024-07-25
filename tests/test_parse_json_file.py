from parse_json_file import parseJSONFile
import pytest


class TestJSONParse:

    def test_invalid_file_path(self):
        path = "./tests/invalid_path"

        with pytest.raises(FileNotFoundError):
            parseJSONFile(path)

    def test_empty_file(self):
        with pytest.raises(ValueError):
            parseJSONFile("validationFiles/test/test2.json")

    def test_valid_path(self):
        path = "validationFiles/test/test1.json"

        actual = parseJSONFile(path)
        expected = {
          "test" : "TestData",
          "anotherProperty": False
        }

        assert actual == expected
