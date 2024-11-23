from pathlib import Path

# パスオブジェクトの作成
current_file = Path("file.txt")
print(current_file)

project_dir = Path("/path/to/project")
print(project_dir)

# 特別なパス
current_dir = Path.cwd()
print(current_dir)

home_dir = Path.home()
print(home_dir)

path = Path("/path/to/file.txt")

# パスの各部分へのアクセス
print(path.parent)  # 親ディレクトリ
print(path.name)  # ファイル名
print(path.stem)  # 拡張子を除いたファイル名
print(path.suffix)  # 拡張子

# パスの結合 (Path オブジェクトにより / 演算子がオーバーロードされている)
new_path = path.parent / "another_file.txt"
print(new_path)

# Pathオブジェクトの作成
file_path = Path("example.txt")

# ファイルの読み書き
content = file_path.read_text(encoding="utf-8")
file_path.write_text("Hello, World!", encoding="utf-8")

# ファイルの存在確認と種類
if file_path.exists():
    print(f"Is file: {file_path.is_file()}")
    print(f"Is directory: {file_path.is_dir()}")

# ファイル検索
# カレントディレクトリのPathオブジェクトを作成
current_dir = Path(".")
# 再帰的にPythonファイルを検索
for python_file in current_dir.glob("**/*.py"):
    print(python_file)