# examples/demo.py

from grapes_tokenizer import GrapesTokenizer

def main():
    tok = GrapesTokenizer(positional=True)
    for w in ["cat", "no", "on", "hello", "abc"]:
        print(f"{w} → {tok.encode(w)}")

if __name__ == "__main__":
    main()
