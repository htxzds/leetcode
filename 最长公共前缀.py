class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        if len(strs)<2: return strs[0]
        i = 0
        minlen = len(strs[0])
        for index,a in enumerate(strs):
            if len(a)< minlen:
                i = index
                minlen = len(a)
        str1 = strs[i]
        
        num = 0
        x = 0
        for index,i in enumerate(str1):
            for str2 in strs:
                if i == str2[index]:
                    num = num+1
                    
                else:
                    x=1
                    break

            if x ==1:
                break

        num =int(num/len(strs))

        if num>0:
            return str1[0:num]
        else:
            return ""
