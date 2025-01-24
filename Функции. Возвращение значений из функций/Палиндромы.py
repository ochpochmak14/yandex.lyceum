def palindrome(s: str) -> str:
    ls = [x.strip() for x in s.split()]
    s = ''.join(ls)
    if s.lower() == s[::-1].lower():
        return "Палиндром"
    return "Не палиндром"