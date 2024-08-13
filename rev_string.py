"""
Remove spaces and reverse string

"the sky is blue"
"blue is sky the"
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = s.split(' ')
        temp = temp[::-1]
        out = ''
        for word in temp:
            if word != '':
                out+=(word+' ')
        return out.strip()
        
