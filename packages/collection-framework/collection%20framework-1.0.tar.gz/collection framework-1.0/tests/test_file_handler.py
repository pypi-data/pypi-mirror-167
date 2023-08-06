import os
import pytest
from unittest.mock import patch, mock_open

from collection_framework.file_handler import read_file

BASE_DIR = os.getcwd()
path_to_example = ['tests', 'examples']

if os.name == 'nt':
    BASE_DIR += '\\' + '\\'.join(path_to_example) + '\\'
else:
    BASE_DIR += '/' + '/'.join(path_to_example) + '/'


class TestFileHandler:
    """Test file_handler.read_file"""

    def setup(self):
        self.func = read_file
        self.path_to_small_file = BASE_DIR + 'small.txt'
        self.path_to_big_file = BASE_DIR + 'big.txt'
        self.patch_to_file_wrong = BASE_DIR + 'WrOnG'

    def test_with_mock_file(self):
        data = '122333hello'
        with patch("builtins.open", mock_open(read_data=data)) as mock_file:
            assert open(self.path_to_small_file).read() == data
        mock_file.assert_called_with(self.path_to_small_file)

    def test_with_small_file_right(self):
        data = self.func(self.path_to_small_file)
        assert data == '122333hello'

    def test_with_small_file_wrong(self):
        data = self.func(self.path_to_small_file)
        assert data != 'WrOnG'

    def test_with_big_file_right(self, capfd):
        self.func(self.path_to_big_file)
        captured = capfd.readouterr()
        assert 'is too big, no more than 5000 characters' in captured.out

    def test_with_big_file_bad(self, capfd):
        self.func(self.path_to_big_file)
        captured = capfd.readouterr()
        assert 'WrOnG' not in captured.out

    def test_with_wrong_patch(self):
        with pytest.raises(FileNotFoundError) as e:
            self.func(self.patch_to_file_wrong)
        assert 'No such file or directory' in str(e.value)



