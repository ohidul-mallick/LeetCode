def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count =0
        cnt =0
        for i in s:
            if i == 'R':
                count +=1
            else:
                count -=1
            if count==0:
                cnt +=1
        return cnt
# Very Important
# Passed