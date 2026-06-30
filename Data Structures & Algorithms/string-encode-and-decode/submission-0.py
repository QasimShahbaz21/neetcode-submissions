class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
           character_numbers = len(word)
           # Add character at the start
           numberappend = f"{character_numbers}#{word}"
           result.append(numberappend)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0  # Our pointer, starting at the beginning of the string
        
        while i < len(s):
            hash_index = s.find('#', i)
            length = int(s[i:hash_index])
            word = s[hash_index + 1: hash_index + 1 + length]
            result.append(word)
            i = hash_index + 1 + length

        return result
