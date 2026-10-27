class Solution:
    # Numbers as prefic with _ delimeter ex: 
    # Input: "Hello World"
    # Output: "55 helloworld:
    # The number 55 represents the length of each word as a combined int
    def encode(self, strs: List[str]) -> str:
        combined = ""
        serial = []
        
        for word in strs:
            combined += word
            serial.append(str(len(word)) + " ")
        
        return "".join(str(num) for num in serial) + "_" + combined

    def decode(self, s: str) -> List[str]:
        serial = []
        len_to_cut = 0
        buffer = 0
        for char in s:
            len_to_cut+=1
            if char == "_":
                break
            if char == " ":
                serial.append(buffer)
                buffer = 0
                continue
            buffer = buffer * 10 + int(char)

        # Split the serial from the encoded strings
        encoded = s[len_to_cut:]

        strs = []
        idx = 0
        # TODO: This cannot read 2 digit numbers
        # Ex: if word is 10 chars long, it will evaluate as word of
        # length 1 and length 0
        # Delimiter for numbers? That is different from prefix break delimiter
        for length in serial:
            strs.append("".join(encoded[idx:length+idx]))
            idx += length

        return strs
