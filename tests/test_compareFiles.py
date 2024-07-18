from parse_json_file import parseJSONFile
from compareFiles import compareFiles


class TestCompareFiles:

    def test_no_diffs(self):
        fileA = parseJSONFile("validationFiles/test5.json")
        fileB = parseJSONFile("validationFiles/test5.json")
        actual = compareFiles(fileA,fileB)
        expected = "No diffs found between files"
        assert actual == expected

    def test_same_data_diff_json_response_files(self):
        fileA = parseJSONFile("validationFiles/test5 copy.json")
        fileB = parseJSONFile("validationFiles/test5.json")
        actual = compareFiles(fileA, fileB)
        expected = "No diffs found between files"
        assert actual == expected

    def test_same_data_diff_json_response_file_reverseFiles(self):
        fileA = parseJSONFile("validationFiles/test5 copy.json")
        fileB = parseJSONFile("validationFiles/test5.json")
        actual = compareFiles(fileB, fileA)
        expected = "No diffs found between files"
        assert actual == expected

    def test_fifty(self):
        fileA = parseJSONFile("validationFiles/dev/101_Asset copy.json")
        fileB = parseJSONFile("validationFiles/dev/101_Asset.json")
        actual = compareFiles(fileA, fileB)
        expected = "No diffs found between files"
        assert actual == expected
    def test_APIResponse(self):
        fileA = parseJSONFile("validationFiles/dev/943_dev_asset.json")
        fileb = parseJSONFile("validationFiles/dev/943_dev_asset copy.json")
        actual = compareFiles(fileA, fileb)
        expected = "Mismatching entities found between files."
        assert actual == expected

    def loadTest(self):
        fileA = parseJSONFile("/Users/cyannuzz/Downloads/hightowerFirmUser.json")
        fileB = parseJSONFile("/Users/cyannuzz/Downloads/hightowerFirmUser.json")
        actual = compareFiles(fileA, fileB)
        expected = "No diffs found between files"
        assert actual == expected
