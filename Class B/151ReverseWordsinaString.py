class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        res = ''
        for word in words:
            if word == ' ':
                words.remove(word)

        for word in words:
            res += word + " "

        return res.strip()


print(f"{Solution().reverseWords(s='the sky is blue')}")
