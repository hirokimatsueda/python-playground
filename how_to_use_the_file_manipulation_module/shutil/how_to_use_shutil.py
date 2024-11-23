import os
from pathlib import Path
import shutil
import time

# 実行前のクリーンアップ
if os.path.isfile("dest.txt"):
    os.remove("dest.txt")
shutil.rmtree("dst_dir", ignore_errors=True)
shutil.rmtree("dest", ignore_errors=True)
os.mkdir("dest")
Path("source.txt").touch()

# ファイルのコピー
shutil.copy("source.txt", "dest.txt")  # ファイルをコピー
shutil.copy2("source.txt", "dest.txt")  # メタデータも含めてコピー

# ディレクトリのコピー
shutil.copytree("src_dir", "dst_dir")  # ディレクトリ全体をコピー
shutil.copytree("src_dir", "dst_dir", dirs_exist_ok=True)  # 上書きコピー

# ファイル・ディレクトリの移動
shutil.move("source.txt", "dest/file.txt")

# ディレクトリの削除
shutil.rmtree("dest")  # 中身ごと削除

# ディレクトリ内の古いファイルの削除
def remove_old_files(directory, days):
    path = Path(directory)
    threshold = time.time() - (days * 86400)
    for item in path.glob("**/*"):
        if item.is_file() and item.stat().st_mtime < threshold:
            item.unlink()

# アーカイブの作成
shutil.make_archive("archive_name", "zip", "directory_to_compress")

# アーカイブの展開
shutil.unpack_archive("archive_name.zip", "extract_dir")