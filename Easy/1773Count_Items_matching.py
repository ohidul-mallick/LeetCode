
def countMatches(items, ruleKey,ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        rule = -1
        count =0
        if ruleKey == "type":
            rule = 0
        elif ruleKey == "color":
            rule = 1
        else:
            rule =2
        for item in items:
            if item[rule] == ruleValue:
                count +=1
        return count

# Passed
