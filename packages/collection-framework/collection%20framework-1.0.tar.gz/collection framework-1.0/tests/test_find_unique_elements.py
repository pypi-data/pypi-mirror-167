import pytest

from collection_framework.collection import find_unique_elements


class TestFindUniqueElements:
    """
    Test function find_unique_elements from collection_framework.collection
    """

    def setup(self):
        self.func = find_unique_elements

    @pytest.mark.parametrize('text, expected_result', [('', 0),
                                                       ('a', 1),
                                                       ('abbbccdf', 3),
                                                       ('AaBb', 4),
                                                       ('1 2', 3)])
    def test_with_different_strings(self, text, expected_result):
        """Tests with normal behavior"""
        assert self.func(text) == expected_result

    def test_with_wrong_result(self):
        """Test with abnormal behavior"""
        assert self.func('aaa') != 1

    def test_wrong_data_type(self):
        """Test with wrong data type, expected raise TypeError"""
        with pytest.raises(TypeError) as e:
            self.func(1)
        assert 'Data must be a string value' in str(e.value)
