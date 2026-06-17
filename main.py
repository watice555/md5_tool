import argparse
import hashlib


def md5_hash(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate the MD5 hash of input text.")
    parser.add_argument("text", nargs="?", help="Text to hash")
    args = parser.parse_args()

    if args.text is not None:
        print(md5_hash(args.text))
        return

    while True:
        try:
            text = input("请输入要计算 MD5 的内容: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break

        print(md5_hash(text))


if __name__ == "__main__":
    main()
