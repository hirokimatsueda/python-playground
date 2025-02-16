import argparse


def parse_args_minimal():
    # ArgumentParserのインスタンスを作成
    parser = argparse.ArgumentParser()

    # 各引数を定義
    parser.add_argument("--input")
    parser.add_argument("--output")
    parser.add_argument("--format", choices=["csv", "json", "markdown"], default="csv")
    parser.add_argument("--force", action="store_true")

    return parser.parse_args()


def main():
    args = parse_args_minimal()

    # 引数の使用例
    print(f"入力ファイル: {args.input}")
    print(f"出力ファイル: {args.output}")
    print(f"出力形式: {args.format}")
    print(f"上書き: {args.force}")


if __name__ == "__main__":
    main()
