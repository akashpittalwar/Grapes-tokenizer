# sumtoken/core.py

class SumTokenizer:
    def __init__(self, positional=False, case_sensitive=False):
        self.positional = positional
        self.case_sensitive = case_sensitive

    def _letter_to_number(self, ch):
        if not self.case_sensitive:
            ch = ch.lower()
        if ch.isalpha():
            return ord(ch) - ord('a') + 1
        return 0  # Ignore non-letters

    def _binary_add(self, bin1, bin2):
        return bin(int(bin1, 2) + int(bin2, 2))[2:]

    def encode(self, word: str) -> int:
        total_bin = '0'
        for idx, ch in enumerate(word):
            num = self._letter_to_number(ch)
            if self.positional:
                num *= (idx + 1)  # Position-based weight
            bin_val = bin(num)[2:]  # Convert to binary (no '0b')
            total_bin = self._binary_add(total_bin, bin_val)
        return int(total_bin, 2)  # Convert final binary sum to decimal
