from src.parse_csv_file import parse_csv
import pytest


class TestCSVParse:

    def test_invalid_file_path(self):
        path = "./tests/invalid_path"

        with pytest.raises(FileNotFoundError):
            parse_csv(path)

    def test_empty_file(self):
        with pytest.raises(ValueError):
            parse_csv("validationFiles/test/test2.json")


    def test_valid_path(self):
        path = "validationFiles/test/test3.csv"

        actual = parse_csv(path)
        expected = [{'Name': 'test', 'id': '1', 'ticker': 'MSFT'}]


        assert actual == expected
