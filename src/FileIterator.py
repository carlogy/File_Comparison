
class FileIterator:
    def __init__(self, file, file2=None):
        self._file = file
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._file):
            item = self._file[self._index]
            self._index += 1
            return item

        else:
            raise StopIteration
