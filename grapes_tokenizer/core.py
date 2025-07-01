# grapes_tokenizer/core.py

class GrapesTokenizer:
    """
    Sum‐based tokenizer with:
      - Letters a–z → 1–26
      - Digits 0–9 → their integer value (0–9)
      - All other characters → ASCII code via ord()
    """

    def __init__(self, positional: bool = False, case_sensitive: bool = False):
        self.positional = positional
        self.case_sensitive = case_sensitive

    def _char_to_value(self, ch: str) -> int:
        # handle case
        if not self.case_sensitive:
            ch = ch.lower()

        # letters
        if ch.isalpha():
            return ord(ch) - ord('a') + 1
        # digits
        if ch.isdigit():
            return int(ch)
        # everything else (punctuation, whitespace, etc.)
        return ord(ch)

    def _binary_add(self, b1: str, b2: str) -> str:
        return bin(int(b1, 2) + int(b2, 2))[2:]

    def encode(self, text: str) -> int:
        """
        Encode a single string and return its decimal token.
        """
        total_bin = '0'
        for idx, ch in enumerate(text):
            val = self._char_to_value(ch)
            if self.positional:
                val *= (idx + 1)
            b = bin(val)[2:]
            total_bin = self._binary_add(total_bin, b)

        return int(total_bin, 2)
