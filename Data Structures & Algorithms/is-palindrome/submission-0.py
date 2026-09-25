class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_s = []
        for char in s:
            if char.isalnum():
                list_s.append(char.lower())
        arr_s_inv = list_s[::-1]
        print(arr_s_inv)
        print(list_s)
        return list_s == arr_s_inv


        