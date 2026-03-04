"""
ProteAlert テキストコントラスト改善パッチ
=========================================
VPS上で実行: python patch_contrast.py

修正: グレー系テキストが薄くて見にくい問題
- --t2 (サブテキスト): #8e94a8 → #a8aec2 (明るく)
- --t3 (ラベル/補足): #565c72 → #737a94 (明るく)
"""

import shutil
from datetime import datetime

FILE = r"C:\protealert\index.html"

# バックアップ
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = FILE.replace(".html", f"_backup_{ts}.html")
shutil.copy2(FILE, backup)
print(f"✅ バックアップ: {backup}")

with open(FILE, "r", encoding="utf-8") as f:
    html = f.read()

# --t2: サブテキスト（商品名、説明文など）
html = html.replace("--t2:#8e94a8", "--t2:#a8aec2")
print("✅ --t2: #8e94a8 → #a8aec2")

# --t3: ラベル、補足テキスト（容量:、更新時刻など）
html = html.replace("--t3:#565c72", "--t3:#737a94")
print("✅ --t3: #565c72 → #737a94")

with open(FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n🎉 コントラスト改善完了！")
print(f'git add -A && git commit -m "Improve text contrast" && git push')
