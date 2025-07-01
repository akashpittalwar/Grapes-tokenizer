# examples/demo.py

from sumtoken.core import SumTokenizer

def main():
    tokenizer = SumTokenizer(positional=True)  # Only decimal output
    words = ["cat", "no", "on", "abc", "hello"]
    for word in words:
        token = tokenizer.encode(word)
        print(f"{word} → {token}")

if __name__ == "__main__":
    main()
