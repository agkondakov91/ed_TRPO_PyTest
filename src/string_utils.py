def reverse(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError('Argument must be a string')
    return s[::-1]


def is_palindrome(s: str) -> bool:
    result = reverse(s)
    return result.lower() == s.lower()


def count_vowels(s: str) -> int:
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

