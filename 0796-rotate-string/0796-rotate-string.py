class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return 0

        temp = s+s
        if goal in temp:
            return 1
        else:
            return 0

        