import os

# 実行前のクリーンアップ
fd = os.open("old.txt", os.O_CREAT)
os.close(fd)

try:
    os.rmdir("path/to/directory/new_directory")
except:
    pass

try:
    os.removedirs("path/to/directory/path/to/deep/dir")
except:
    pass

# ファイルの存在確認
if os.path.exists("old.txt"):
    print("ファイルが存在します")

# ファイル操作
os.rename("old.txt", "new.txt")  # ファイル名変更
os.remove("new.txt")  # ファイル削除
os.chmod("file.txt", 0o755)  # 権限変更

# ファイル情報の取得
size = os.path.getsize("file.txt")
mtime = os.path.getmtime("file.txt")  # 最終更新時刻
print(f"size = {size}, mtime = {mtime}")

# カレントディレクトリの取得と変更
current_dir = os.getcwd()
os.chdir("path/to/directory")

# ディレクトリ作成
os.mkdir("new_directory")  # 単一ディレクトリ
os.makedirs("path/to/deep/dir")  # 途中のディレクトリも作成

# ディレクトリ内のディレクトリやファイルの一覧取得
files = os.listdir(".")
print(files)

# パスの結合
full_path = os.path.join("directory", "subdirectory", "file.txt")
print(full_path)  # directory/subdirectory/file.txt

# パスの分割
dir_name = os.path.dirname("/path/to/file.txt")
print(dir_name)  # /path/to

base_name = os.path.basename("/path/to/file.txt")
print(base_name)  # file.txt

root, ext = os.path.splitext("file.txt")
print(f"root = {root}, ext = {ext}")  # root = file, ext = .txt