class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to hold our groups
        # Key: sorted word (string) -> Value: list of original words
        anagram_map = {}
        
        for word in strs:
            # 1. Sort the word alphabetically. 
            # sorted("nat") returns ['a', 'n', 't']. 
            # "".join() turns it back into a string: "ant"
            sorted_word = "".join(sorted(word))
            
            # 2. If this sorted signature isn't in our map, create a new bucket
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []
                
            # 3. Append the ORIGINAL word to its sorted bucket
            anagram_map[sorted_word].append(word)
            
        # 4. Return just the grouped lists from the dictionary values
        return list(anagram_map.values())