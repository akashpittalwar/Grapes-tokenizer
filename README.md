# 🍇 Grapes Tokenizer

A simple, sum-based tokenizer for quick NLP experiments and LLM research.

**Grapes Tokenizer** maps each character to a numeric value, applies positional weighting, packs into binary “chunks,” then returns a single decimal token per input string:

- **Letters** `a`–`z` → 1–26  
- **Digits** `0`–`9` → 0–9  
- **Specials** (punctuation, whitespace, symbols) → their ASCII code  
- **Positional weighting** (always on): each char’s value × (index + 1)  
- **Binary-add** each weighted value, then convert back to decimal

---

## 🚀 Features

- 🔢 **Deterministic**: same input → same token  
- 🔒 **Reversible** for short segments via bit-packing (see examples)  
- ⚠️ **Non-unique** for long strings (collisions possible)—best for hashing/obfuscation  
- 📦 **Lightweight**: zero dependencies, pure Python  
- 🛠️ **Extensible**: wrap as a subword tokenizer or custom PreTokenizer  

---

## 💾 Installation

```bash
pip install grapes-tokenizer
