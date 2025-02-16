import argparse
import os
import sys
from pathlib import Path


def validate_input_file(path):
    """入力ファイルの存在確認とパスの絶対パス化"""
    path_obj = Path(path).resolve()
    if not path_obj.exists():
        raise argparse.ArgumentTypeError(f"入力ファイルが存在しません: {path}")
    return str(path_obj)


def validate_output_path(path):
    """出力パスのバリデーションと絶対パス化"""
    path_obj = Path(path).resolve()
    dir_path = path_obj.parent
    # 出力ディレクトリの存在確認
    if not dir_path.exists():
        raise argparse.ArgumentTypeError(
            f"出力先ディレクトリが存在しません: {dir_path}"
        )
    # 書き込み権限の確認
    if not os.access(dir_path, os.W_OK):
        raise argparse.ArgumentTypeError(
            f"出力先ディレクトリに書き込み権限がありません: {dir_path}"
        )
    return str(path_obj)


def parse_args_advanced():
    parser = argparse.ArgumentParser(
        description="データ形式変換スクリプト",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  %(prog)s -i input.csv -o output.json --format json
  %(prog)s -i data.json -o result.md --force
        """,
    )

    # 入出力の設定
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        type=validate_input_file,
        help="入力ファイルパス",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=validate_output_path,
        help="出力ファイルパス",
    )

    # 変換オプション
    parser.add_argument(
        "--format",
        choices=["csv", "json", "markdown"],
        default="json",
        help="出力形式 (デフォルト: json)",
    )

    # 動作オプション
    parser.add_argument(
        "--force", action="store_true", help="既存の出力ファイルを上書きする"
    )

    args = parser.parse_args()

    # 出力ファイルの存在確認
    if not args.force and Path(args.output).exists():
        parser.error(
            f"出力ファイルが既に存在します: {args.output}\n"
            f"上書きする場合は --force オプションを指定してください"
        )

    return args


def main():
    args = parse_args_advanced()

    try:
        # ここに実際の変換処理を実装
        print(f"入力ファイル: {args.input}")
        print(f"出力ファイル: {args.output}")
        print(f"出力形式: {args.format}")
        print(f"上書き: {args.force}")

    except Exception as e:
        print(f"エラーが発生しました: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
