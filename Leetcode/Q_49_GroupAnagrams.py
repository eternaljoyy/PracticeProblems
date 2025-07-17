class Solution(object):
    def groupAnagrams(self, strs):
        """
        Ex A) strs = ["eat","tea","tan","ate","nat","bat"] 

         -> 'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'] 

        ========================================================
        M = # of items in the strs array 
        
        Spacetime Complexity: O(N)
        - worst case would occur when you add every single 
        item to the newly created dictionary, resulting in a time 
        complexity of O(N). 


        Runtime Complexity: O(M* NlogN)
        - first loop takes O(M), as its going through each item 
        in strs array one by one. 
        - sorted() function runtime is O(nlogn)
        """

        group_anagrams = {}
        

        #find the and return the group anagrams 
        for item in range(len(strs)):
            sorted_word = ''.join(sorted(strs[item]))
            
            if sorted_word not in group_anagrams:
                group_anagrams[sorted_word] = [strs[item]]
            else:
                group_anagrams[sorted_word].append(strs[item])
        return list(group_anagrams.values())



# testcases 
first_anagram = Solution() 
print(first_anagram.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

second_anagram = Solution() 
print(second_anagram.groupAnagrams(["a"]))

third_anagram = Solution()
print(third_anagram.groupAnagrams([""]))