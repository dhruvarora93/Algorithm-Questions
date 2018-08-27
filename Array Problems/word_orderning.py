def delete_palindrome(s, k):

    def helper(left, right):
        if left >= right:
            return 0

        if s[left] == s[right]:
            return helper(left+1, right-1)

        delete_left = 1 + helper(left+1, right)
        delete_right = 1 + helper(left, right-1)
        return min(delete_left, delete_right)

    return helper(0, len(s)-1) <= k



print(delete_palindrome("npamacdn",3))