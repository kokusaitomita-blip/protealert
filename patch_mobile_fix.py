"""
ProteAlert モバイル表示修正パッチ
==================================
VPS上で実行: python patch_mobile_fix.py

修正内容:
1. モバイルでnav-wrapをfixed bottom化（.navだけでなく親も）
2. Heroのflex-wrap挙動を修正
"""

import os
import shutil
from datetime import datetime

# === 設定 ===
FILE = r"C:\protealert\index.html"

# === バックアップ ===
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = FILE.replace(".html", f"_backup_{ts}.html")
shutil.copy2(FILE, backup)
print(f"✅ バックアップ作成: {backup}")

# === 読み込み ===
with open(FILE, "r", encoding="utf-8") as f:
    html = f.read()

# ============================================================
# PATCH 1: モバイル nav → nav-wrap を fixed bottom に変更
# ============================================================

OLD_MOBILE_NAV = """.nav{position:fixed;bottom:0;left:0;right:0;background:rgba(8,9,13,.92);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-top:1px solid var(--border);z-index:100;justify-content:center;width:100%;border-radius:0;border:none;padding:.5rem .75rem}"""

NEW_MOBILE_NAV = """.nav-wrap{position:fixed;bottom:0;left:0;right:0;background:rgba(8,9,13,.92);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-top:1px solid var(--border);z-index:100;padding:.4rem .75rem}
  .nav{width:100%;border:none;border-radius:0;background:transparent;padding:0;justify-content:center}"""

html = html.replace(OLD_MOBILE_NAV, NEW_MOBILE_NAV)
print("✅ PATCH 1: nav-wrap fixed bottom化")

# ============================================================
# PATCH 2: Hero card の flex-wrap を削除しモバイルで確実に縦積み
# ============================================================

# デスクトップCSS: flex-wrap:wrap を削除
OLD_HERO_CARD = """.hero-card{background:var(--grad-hero);border:1px solid rgba(0,232,143,.12);border-radius:var(--r);padding:1.5rem 2rem;display:flex;align-items:center;justify-content:space-between;gap:1.5rem;flex-wrap:wrap;position:relative;overflow:hidden;animation:fu .5s ease both}"""

NEW_HERO_CARD = """.hero-card{background:var(--grad-hero);border:1px solid rgba(0,232,143,.12);border-radius:var(--r);padding:1.5rem 2rem;display:flex;align-items:center;justify-content:space-between;gap:1.5rem;position:relative;overflow:hidden;animation:fu .5s ease both}"""

html = html.replace(OLD_HERO_CARD, NEW_HERO_CARD)
print("✅ PATCH 2: Hero flex-wrap削除（モバイルはflex-directionで制御）")

# ============================================================
# PATCH 3: モバイル Hero のpadding/gap を調整
# ============================================================

OLD_HERO_MOBILE = """.hero-card{padding:1.1rem 1.2rem;flex-direction:column;align-items:flex-start}
  .hero-right{align-items:flex-start}
  .hero-ppg{font-size:2.1rem}
  .hero-updated{text-align:left}"""

NEW_HERO_MOBILE = """.hero-card{padding:1.1rem 1.2rem;flex-direction:column;align-items:flex-start;gap:1rem}
  .hero-right{align-items:flex-start;width:100%}
  .hero-ctas{width:100%}
  .hero-cta{flex:1;justify-content:center}
  .hero-ppg{font-size:2.1rem}
  .hero-updated{text-align:left}"""

html = html.replace(OLD_HERO_MOBILE, NEW_HERO_MOBILE)
print("✅ PATCH 3: モバイル Hero レイアウト改善")

# ============================================================
# 書き出し
# ============================================================
with open(FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n🎉 モバイル修正完了！")
print(f"   バックアップ: {backup}")
print(f"\n📋 次のステップ:")
print(f"   git add -A && git commit -m 'Fix mobile hero and bottom nav' && git push")
