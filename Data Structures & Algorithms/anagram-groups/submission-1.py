class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list = {}

        for words in strs:
                sorted_order= "".join(sorted(words))
                if sorted_order in new_list:
                    new_list[sorted_order].append(words)
                else:
                    new_list[sorted_order] = [words]

        return list(new_list.values())
