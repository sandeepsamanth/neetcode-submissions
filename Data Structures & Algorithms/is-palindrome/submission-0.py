class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string=""

        for i in s:
            if i.isalnum():
                cleaned_string+=i.lower()
        print(cleaned_string)
        print(cleaned_string[::-1])
        return cleaned_string==cleaned_string[::-1]
        