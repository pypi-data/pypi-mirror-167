import pytest
import os


from collection_framework.cli_interface import main


BASE_DIR = os.getcwd()
BASE_DIR = os.path.join(BASE_DIR, 'tests', 'examples')


class TestCLIInterfaceMain:
    """Test CLI Interface"""

    def setup(self):
        self.func = main
        self.path_to_small_file = os.path.join(BASE_DIR, 'small.txt')

    def test_main_with_no_options(self, capfd):
        self.func()
        captured = capfd.readouterr()
        assert 'Nothing to do. Use -h option for help.' in captured.out

    def test_main_with_text(self, capfd):
        self.func(text='hello')
        captured = capfd.readouterr()
        assert 'Unique elements in string: 3' in str(captured)

    def test_main_with_wrong_file(self, capfd):
        self.func(file='hello.txt')
        captured = capfd.readouterr()
        assert 'hello.txt not found' in str(captured)

    def test_main_with_small_file(self, capfd):
        self.func(file=self.path_to_small_file)
        captured = capfd.readouterr()
        assert 'Unique elements in txt file: 4' in str(captured)




