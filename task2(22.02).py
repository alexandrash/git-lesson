s = str(input('Введите выражение:'))

def check_palindrome(s):
    s = s.split()
    s = ''.join(s)

    i = 0
    l = len(s)

    while i <= l // 2:
        if s[i] != s[l- 1- i]:
            return False
        i += 1

    else:
        return True

print (check_palindrome(s))

