class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped = {}
        def sortString(s):
            for inputStr in s:
                sortedStr = ''.join(sorted(inputStr))
                if (sortedStr in mapped.keys()):
                    mapped[sortedStr].append(inputStr)
                else:
                    mapped[sortedStr]=[inputStr]

        sortString(strs)
        return (list(mapped.values()))
        

        
