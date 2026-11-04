class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str in strs:    
            length = len(str)
            res += f"{length}#" + str
        
        return res

    def decode(self, s: str) -> List[str]:
        input_length = len(s)
        res = []
        decoded_chars = 0
        while decoded_chars < input_length:
            number_string = ""
            while s[decoded_chars].isdigit():
                number_string += s[decoded_chars]
                decoded_chars += 1

            string_length = int(number_string)
            decoded_chars += 1 

            res.append(s[decoded_chars:decoded_chars + string_length])
            decoded_chars += string_length
        return res
            