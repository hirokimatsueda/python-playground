# テキストファイルの書き込み
with open('sample.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World!\n')
    f.writelines(['First line\n', 'Second line\n'])

# テキストファイルの読み込み
with open('sample.txt', 'r', encoding='utf-8') as f:
    # ファイル全体を1つの文字列として読み込み
    content = f.read()

    # ファイルを最初から読み直す
    f.seek(0)

    # 1行ずつ読み込み
    for line in f:
        print(line.strip())

# 書き込み専用 ('w') - ファイルを新規作成または上書き
with open("file.txt", "w") as f:
    f.write("new content")

# 読み込み専用 ('r')
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

# 追記モード ('a')
with open("log.txt", "a") as f:
    f.write("新しいログエントリ\n")

# バイナリモード ('rb', 'wb')
with open("image.png", "rb") as f:
    binary_data = f.read()
    print("{0:02x}".format(binary_data[0]))  # バイナリの先頭 1 バイトを出力

try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('ファイルが存在しません')
except PermissionError:
    print('ファイルにアクセスする権限がありません')