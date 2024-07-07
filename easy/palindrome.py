def isPalindrome(x) -> bool:
    palindrome_check = str(x)
    length = len(palindrome_check)
    if length >1:
        for i in range(int(length / 2 + length % 2)):
            j = len(palindrome_check) - 1 - i
            if (palindrome_check[i] != palindrome_check[j]):
                return False
        return True
    else:
        return False

print(isPalindrome("m"))
