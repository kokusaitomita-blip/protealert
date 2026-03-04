"""
ProteAlert Nav 4タブ対応パッチ
==============================
VPS上で実行: python patch_nav4.py

修正: .nav の width:fit-content を削除して4タブが収まるようにする
"""

import shutil
from datetime import datetime

FILE = r"C:\protealert\index.html"

ts = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = FILE.replace(".html", f"_backup_{ts}.html")
shutil.copy2(FILE, backup)
print(f"✅ バックアップ: {backup}")

with open(FILE, "r", encoding="utf-8") as f:
    html = f.read()

# デスクトップ: width:fit-content を削除
html = html.replace(
    ".nav{display:flex;gap:.35rem;background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:4px;width:fit-content}",
    ".nav{display:flex;gap:.35rem;background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:4px}"
)
print("✅ PATCH 1: .nav width:fit-content 削除")

with open(FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f'\n🎉 完了！')
print(f'git add -A && git commit -m "Fix nav width for 4 tabs" && git push')
