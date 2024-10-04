class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber>0:
            remainder = (columnNumber-1)%26
            result = chr(ord("A")+remainder)+result
            columnNumber=(columnNumber-1)//26
        return result
        