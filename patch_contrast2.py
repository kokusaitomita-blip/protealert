"""
ProteAlert テキストコントラスト強化 v2
======================================
VPS上で実行: python patch_contrast2.py

前回パッチ適用済の値からさらに明るく:
- --t2: #a8aec2 → #eaecf2 (白=t1と同じ)
- --t3: #737a94 → #b0b6c8 (明るめグレー)
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

html = html.replace("--t2:#a8aec2", "--t2:#eaecf2")
print("✅ --t2: #a8aec2 → #eaecf2 (白)")

html = html.replace("--t3:#737a94", "--t3:#b0b6c8")
print("✅ --t3: #737a94 → #b0b6c8 (明るめグレー)")

with open(FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f'\n🎉 完了！')
print(f'git add -A && git commit -m "Boost text contrast v2" && git push')
