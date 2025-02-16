# How to use unittest mock

Blog post: [Python の unittest で Mock を使用しテストの幅を広げる - Qiita](https://qiita.com/pokapu/items/bb4d6bd7645ca4820235)

## How to run these tests

1. Create venv

   ```bash
   python -m venv .venv
   ```

2. Activate venv
   - Windows:
     ```pwsh
      .\.venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
3. Install libraries

   ```bash
   pip install -r requirements.txt
   ```

4. Run tests

   ```bash
   python -m unittest main.py -v
   ```
