from solver import Solution

sol = Solution()

def test_palindrome():
    assert sol.isPalindrome(121) == True

def test_not_palindrome_negative():
    assert sol.isPalindrome(-121) == False

def test_not_palindrome():
    assert sol.isPalindrome(21) == False
