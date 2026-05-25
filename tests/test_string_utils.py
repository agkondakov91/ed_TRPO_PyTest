from src.string_utils import reverse, is_palindrome, count_vowels
import pytest


def test_reverse():
    # Arrange
    string = 'Hello, World!'
    expected = '!dlroW ,olleH'

    # Act
    result = reverse(string)

    # Assert
    assert result == expected


def test_reverse_empty_string():
    assert reverse('') == ''


def test_reverse_non_string():
    with pytest.raises(TypeError):
        reverse([1, 2, 3])


def test_is_palindrome():
    # Arrange
    string = 'radar'
    expected = True

    # Act
    result = is_palindrome(string)

    # Assert
    assert result == expected


def test_is_palindrome_with_upper():
    assert is_palindrome('RadAr')


def test_is_not_palindrome():
    assert not is_palindrome('hello')


def test_count_vowels():
    # Arrange
    string = 'I love you, Alice'
    expected = 8

    # Act
    result = count_vowels(string)

    # Assert
    assert result == expected


def test_count_vowels_with_empty_string():
    assert count_vowels('') == 0