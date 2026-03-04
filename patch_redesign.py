"""
ProteAlert デザインリニューアル パッチスクリプト
==============================================
VPS上で実行: python patch_redesign.py

動作:
1. index.html のバックアップを作成
2. CSS全体を洗練版に置換
3. Header / Hero / Nav のHTML構造を更新
4. ランキングテーブルのclass名を更新（JS renderRank対応）
5. アラートカードのclass名を更新（JS renderAlerts対応）
6. renderRank / renderAlerts のJS出力HTMLを新class名に更新
"""

import os
import shutil
from datetime import datetime

# === 設定 ===
FILE = r"C:\\protealert\\index.html"  # VPS上のパス

# === バックアップ ===
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = FILE.replace(".html", f"_backup_{ts}.html")
shutil.copy2(FILE, backup)
print(f"✅ バックアップ作成: {backup}")

# === 読み込み ===
with open(FILE, "r", encoding="utf-8") as f:
    html = f.read()

# ============================================================
# PATCH 1: CSS全置換（<style>...</style> の中身を丸ごと差し替え）
# ============================================================

NEW_CSS = r"""<style>
/* ===== Design System ===== */
:root{--bg:#08090d;--bg-elevated:#0e1017;--bg-card:#12141c;--bg-card-h:#181b26;--bg-surface:#1a1d28;--border:#1c1f2e;--border-subtle:#15172280;--t1:#eaecf2;--t2:#8e94a8;--t3:#565c72;--cyan:#00d4ff;--cyan-dim:rgba(0,212,255,.08);--cyan-mid:rgba(0,212,255,.15);--green:#00e88f;--green-dim:rgba(0,232,143,.06);--green-mid:rgba(0,232,143,.12);--red:#ff4466;--amber:#ffb844;--orange:#ff9900;--purple:#7b5cff;--purple-dim:rgba(123,92,255,.1);--grad:linear-gradient(135deg,#00d4ff,#7b5cff);--grad-brand:linear-gradient(135deg,#00d4ff 0%,#00e88f 100%);--grad-hero:linear-gradient(135deg,rgba(0,232,143,.06),rgba(0,212,255,.04));--r:14px;--r-sm:8px;--r-xs:6px;--shadow-hover:0 8px 32px rgba(0,0,0,.4),0 0 0 1px rgba(0,212,255,.15);--transition:.2s cubic-bezier(.4,0,.2,1);--max-w:1120px}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Noto Sans JP',system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--t1);line-height:1.65;min-height:100vh;-webkit-font-smoothing:antialiased}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 80% 50% at 50% -20%,rgba(0,212,255,.04) 0%,transparent 60%),radial-gradient(ellipse 60% 40% at 80% 100%,rgba(0,232,143,.03) 0%,transparent 50%);pointer-events:none;z-index:0}

/* Header */
header{position:sticky;top:0;z-index:100;background:rgba(8,9,13,.85);backdrop-filter:blur(24px) saturate(1.4);-webkit-backdrop-filter:blur(24px) saturate(1.4);border-bottom:1px solid var(--border-subtle);padding:0 1.5rem}
.h-inner{max-width:var(--max-w);margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:56px;gap:1rem}
.logo{display:flex;align-items:center;gap:.6rem;text-decoration:none}
.logo-ic{width:30px;height:30px;background:var(--grad-brand);border-radius:var(--r-xs);display:flex;align-items:center;justify-content:center;font-size:.85rem;box-shadow:0 0 12px rgba(0,212,255,.2)}
.logo h1{font-size:1.05rem;font-weight:900;letter-spacing:-.02em;background:var(--grad-brand);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.h-right{display:flex;align-items:center;gap:1rem}
.search-box{position:relative}
.search-box input{background:var(--bg-elevated);border:1px solid var(--border);border-radius:var(--r-sm);padding:.5rem .75rem .5rem 2rem;color:var(--t1);font-family:inherit;font-size:.8rem;width:180px;outline:none;transition:all var(--transition)}
.search-box input:focus{border-color:rgba(0,212,255,.4);background:var(--bg-surface);box-shadow:0 0 0 3px rgba(0,212,255,.08)}
.search-box input::placeholder{color:var(--t3)}
.search-box::before{content:'🔍';position:absolute;left:8px;top:50%;transform:translateY(-50%);font-size:.7rem}
.upd{display:flex;align-items:center;gap:6px;font-family:'JetBrains Mono',monospace;font-size:.7rem;color:var(--t3);white-space:nowrap}
.upd-dot{width:6px;height:6px;background:var(--green);border-radius:50%;box-shadow:0 0 6px rgba(0,232,143,.5);animation:pulse 2.5s ease infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}

/* Hero */
.hero{max-width:var(--max-w);margin:0 auto;padding:1.5rem 1.5rem .5rem;position:relative;z-index:1}
.hero-card{background:var(--grad-hero);border:1px solid rgba(0,232,143,.12);border-radius:var(--r);padding:1.5rem 2rem;display:flex;align-items:center;justify-content:space-between;gap:1.5rem;flex-wrap:wrap;position:relative;overflow:hidden;animation:fu .5s ease both}
.hero-card::before{content:'';position:absolute;top:-40%;right:-10%;width:300px;height:300px;background:radial-gradient(circle,rgba(0,232,143,.06) 0%,transparent 70%);pointer-events:none}
.hero-left{display:flex;flex-direction:column;gap:.25rem;position:relative}
.hero-label{font-size:.65rem;color:var(--t3);text-transform:uppercase;letter-spacing:1.5px;font-weight:500}
.hero-ppg{font-family:'JetBrains Mono',monospace;font-size:2.6rem;font-weight:700;color:var(--green);line-height:1.1;letter-spacing:-.02em}
.hero-brand{font-size:.9rem;color:var(--cyan);font-weight:700;margin-top:.1rem}
.hero-product{font-size:.78rem;color:var(--t2);max-width:380px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.hero-right{display:flex;flex-direction:column;align-items:flex-end;gap:.5rem;position:relative}
.hero-price{font-family:'JetBrains Mono',monospace;font-size:1.4rem;font-weight:700}
.hero-ctas{display:flex;gap:.5rem}
.hero-cta{display:inline-flex;align-items:center;gap:.35rem;padding:.6rem 1.2rem;border-radius:var(--r-sm);font-family:inherit;font-size:.8rem;font-weight:600;cursor:pointer;text-decoration:none;transition:all var(--transition);white-space:nowrap;border:1px solid rgba(0,232,143,.3);background:var(--green-mid);color:var(--green)}
.hero-cta:hover{background:rgba(0,232,143,.22);border-color:rgba(0,232,143,.5);transform:translateY(-1px);box-shadow:0 4px 16px rgba(0,232,143,.15)}
.hero-cta-az{background:rgba(255,153,0,.1)!important;border-color:rgba(255,153,0,.25)!important;color:var(--orange)!important}
.hero-cta-az:hover{background:rgba(255,153,0,.18)!important;border-color:rgba(255,153,0,.45)!important;box-shadow:0 4px 16px rgba(255,153,0,.12)!important}
.hero-updated{font-family:'JetBrains Mono',monospace;font-size:.65rem;color:var(--t3);margin-top:.5rem;text-align:right}

/* Nav */
.nav-wrap{max-width:var(--max-w);margin:0 auto;padding:.75rem 1.5rem;position:relative;z-index:1}
.nav{display:flex;gap:.35rem;background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:4px;width:fit-content}
.nav button{padding:.5rem 1rem;border:none;border-radius:var(--r-xs);background:transparent;color:var(--t2);font-family:inherit;font-size:.8rem;font-weight:500;cursor:pointer;transition:all var(--transition);min-height:38px}
.nav button:hover{color:var(--t1);background:rgba(255,255,255,.04)}
.nav button.active{background:rgba(0,212,255,.1);color:var(--cyan);font-weight:600}

main{max-width:var(--max-w);margin:0 auto;padding:0 1.5rem 3rem;position:relative;z-index:1}
.sec{display:none}.sec.active{display:block}
h2{font-size:1.05rem;font-weight:700;margin:1.5rem 0 1rem;display:flex;align-items:center;gap:.4rem}

/* Stats */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:.75rem;margin-bottom:1.5rem}
.st{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--r);padding:1rem 1.1rem;transition:all var(--transition);animation:fu .35s ease both}
.st:nth-child(1){animation-delay:.04s}.st:nth-child(2){animation-delay:.08s}.st:nth-child(3){animation-delay:.12s}.st:nth-child(4){animation-delay:.16s}
.st:hover{border-color:rgba(255,255,255,.06);transform:translateY(-1px)}
.st-l{font-size:.65rem;color:var(--t3);text-transform:uppercase;letter-spacing:.8px;font-weight:500;margin-bottom:.35rem}
.st-v{font-family:'JetBrains Mono',monospace;font-size:1.5rem;font-weight:700;line-height:1.2}
.st-v.cy{color:var(--cyan)}.st-v.gr{color:var(--green)}.st-v.am{color:var(--amber)}.st-v.pu{color:var(--purple)}
.st-s{font-size:.7rem;color:var(--t2);margin-top:.2rem}

/* Filters */
.ctrl{display:flex;gap:.4rem;margin-bottom:1rem;flex-wrap:wrap;align-items:center}
.ctrl-l{font-size:.7rem;color:var(--t3);margin-right:.3rem;font-weight:500}
.pill{padding:.35rem .7rem;border:1px solid var(--border);border-radius:20px;background:transparent;color:var(--t2);font-family:inherit;font-size:.72rem;font-weight:500;cursor:pointer;transition:all var(--transition);min-height:30px}
.pill:hover{border-color:rgba(0,212,255,.3);color:var(--cyan)}
.pill.active{background:var(--cyan-dim);border-color:rgba(0,212,255,.35);color:var(--cyan)}

/* Table */
.tbl-wrap{width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch}
.tbl{width:100%;border-collapse:separate;border-spacing:0 3px}
.tbl th{font-size:.65rem;font-weight:500;color:var(--t3);text-transform:uppercase;letter-spacing:.8px;text-align:left;padding:.5rem .8rem;cursor:pointer;user-select:none;white-space:nowrap;transition:color var(--transition);border-bottom:1px solid var(--border)}
.tbl th:hover{color:var(--cyan)}.tbl th.sa{color:var(--cyan)}
.tr{background:var(--bg-card);transition:all var(--transition);animation:fu .3s ease both}
.tr:hover{background:var(--bg-card-h)}
.tr td{padding:.7rem .8rem;vertical-align:middle;border-top:1px solid transparent;border-bottom:1px solid transparent}
.tr td:first-child{border-radius:var(--r-sm) 0 0 var(--r-sm);border-left:1px solid transparent}
.tr td:last-child{border-radius:0 var(--r-sm) var(--r-sm) 0;border-right:1px solid transparent}
.tr:hover td{border-color:var(--border)}
.tr:nth-child(1){animation-delay:.02s}.tr:nth-child(2){animation-delay:.04s}.tr:nth-child(3){animation-delay:.06s}
.tr:nth-child(4){animation-delay:.08s}.tr:nth-child(5){animation-delay:.1s}.tr:nth-child(6){animation-delay:.12s}
.tr:nth-child(7){animation-delay:.14s}.tr:nth-child(8){animation-delay:.16s}.tr:nth-child(9){animation-delay:.18s}.tr:nth-child(10){animation-delay:.2s}
.rk{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:.9rem;width:2rem;display:inline-flex;align-items:center;justify-content:center}
.r1{color:var(--amber)}.r2{color:#b0b8c8}.r3{color:#c08850}
.pb{font-size:.65rem;color:var(--cyan);font-weight:500;letter-spacing:.3px}
.pn{font-size:.78rem;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:280px}
.ppg{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:1rem;color:var(--green)}
.prc{font-family:'JetBrains Mono',monospace;font-weight:600;font-size:.88rem}
.b{display:inline-flex;align-items:center;padding:.15rem .45rem;border-radius:4px;font-size:.65rem;font-weight:500}
.bw{background:var(--purple-dim);color:var(--purple)}
.bo{background:var(--green-dim);color:var(--green)}
.br{background:rgba(255,68,102,.08);color:var(--red)}
.bs{background:var(--red);color:#fff;font-size:.6rem;padding:.1rem .35rem;margin-left:.3rem;font-weight:600}
.cta{display:inline-flex;align-items:center;gap:.25rem;padding:.3rem .6rem;border-radius:var(--r-xs);font-family:inherit;font-size:.68rem;font-weight:500;cursor:pointer;text-decoration:none;transition:all var(--transition);white-space:nowrap;border:1px solid}
.cta-p{background:var(--cyan-dim);border-color:rgba(0,212,255,.2);color:var(--cyan)}
.cta-p:hover{background:var(--cyan-mid);border-color:rgba(0,212,255,.4)}
.cta-az{background:rgba(255,153,0,.08);border-color:rgba(255,153,0,.2);color:var(--orange)}
.cta-az:hover{background:rgba(255,153,0,.15);border-color:rgba(255,153,0,.4)}
.td-links{display:flex;gap:.35rem}

/* Mobile Cards */
.mcards{display:none}
.mc{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--r);padding:1rem;margin-bottom:.6rem;transition:all var(--transition);animation:fu .3s ease both}
.mc:hover{border-color:rgba(255,255,255,.06)}
.mc-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:.3rem}
.mc-rk{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:1.05rem}
.mc-ppg{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:1.1rem;color:var(--green)}
.mc-br{font-size:.68rem;color:var(--cyan);font-weight:500}
.mc-nm{font-size:.8rem;color:var(--t2);margin:.2rem 0 .5rem;line-height:1.4}
.mc-meta{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap;margin-bottom:.6rem}
.mc-pr{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:.9rem}
.mc-cta{display:flex;gap:.4rem}

/* Alerts */
.alcards{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:.75rem}
.alc{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--r);padding:1.1rem;transition:all var(--transition);position:relative;overflow:hidden;animation:fu .4s ease both}
.alc::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--grad-brand);opacity:.6}
.alc:hover{border-color:rgba(0,212,255,.2);transform:translateY(-2px);box-shadow:var(--shadow-hover)}
.alc:nth-child(1){animation-delay:.05s}.alc:nth-child(2){animation-delay:.1s}.alc:nth-child(3){animation-delay:.15s}.alc:nth-child(4){animation-delay:.2s}
.al-type{font-size:.62rem;font-weight:600;letter-spacing:.8px;text-transform:uppercase;color:var(--cyan);margin-bottom:.4rem}
.al-brand{font-size:.95rem;font-weight:700;margin-bottom:.15rem}
.al-detail{font-size:.78rem;color:var(--t2);margin-bottom:.5rem;line-height:1.4}
.al-save{font-family:'JetBrains Mono',monospace;font-size:1.3rem;font-weight:700;color:var(--green)}
.al-prices{display:flex;gap:.75rem;margin-top:.6rem;padding-top:.6rem;border-top:1px solid var(--border);flex-wrap:wrap}
.al-pi{font-size:.7rem;color:var(--t2)}
.al-pi strong{font-family:'JetBrains Mono',monospace;color:var(--t1);font-weight:600}
#noAlerts{display:none;color:var(--t3);text-align:center;padding:4rem 2rem;font-size:.85rem}

/* Chart */
.ch-wrap{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--r);padding:1.25rem;margin-top:1rem}
.ch-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:.75rem;flex-wrap:wrap;gap:.5rem}
.ch-title{font-size:.9rem;font-weight:700}
.ch-periods{display:flex;gap:.3rem}
.ch-legend{display:flex;gap:.75rem;font-size:.7rem;color:var(--t2);flex-wrap:wrap;margin-bottom:.6rem}
.ch-dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:4px;vertical-align:middle}
#priceChart{max-height:300px}
.ch-note{color:var(--t3);font-size:.68rem;margin-top:.6rem;text-align:center}

footer{max-width:var(--max-w);margin:0 auto;padding:2rem 1.5rem;border-top:1px solid var(--border);text-align:center;color:var(--t3);font-size:.7rem;position:relative;z-index:1}
footer a{color:var(--cyan);text-decoration:none}
footer a:hover{text-decoration:underline}
@keyframes fu{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}

@media(max-width:768px){
  header{padding:0 1rem}
  .h-inner{height:50px}
  .search-box input{width:140px}
  .nav{position:fixed;bottom:0;left:0;right:0;background:rgba(8,9,13,.92);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-top:1px solid var(--border);z-index:100;justify-content:center;width:100%;border-radius:0;border:none;padding:.5rem .75rem}
  .nav button{flex:1;font-size:.75rem;padding:.45rem .5rem}
  main{padding:0 1rem 5rem}
  .hero{padding:1rem 1rem .3rem}
  .hero-card{padding:1.1rem 1.2rem;flex-direction:column;align-items:flex-start}
  .hero-right{align-items:flex-start}
  .hero-ppg{font-size:2.1rem}
  .hero-updated{text-align:left}
  .stats{grid-template-columns:repeat(2,1fr);gap:.5rem}
  .st-v{font-size:1.3rem}
  .tbl-wrap{display:none}.mcards{display:block}
  .alcards{grid-template-columns:1fr}
  h2{font-size:.95rem}
}
@media(max-width:480px){
  .search-box{display:none}
  .hero-ppg{font-size:1.8rem}
  .stats{gap:.4rem}.st{padding:.75rem .85rem}.st-v{font-size:1.15rem}
  .hero-ctas{flex-direction:column;gap:.35rem}
}
</style>"""

import re
# CSS置換
html = re.sub(r'<style>.*?</style>', NEW_CSS, html, count=1, flags=re.DOTALL)
print("✅ PATCH 1: CSS全置換完了")

# ============================================================
# PATCH 2: Hero CTAボタン構造の更新
# ============================================================

# 旧: 2つのaタグが縦並び
OLD_HERO_RIGHT = """    <div class="hero-right">
      <div class="hero-price" id="hero-price">--</div>
      <a href="#" id="hero-cta" class="hero-cta" target="_blank" rel="noopener">最安を見る →</a>
      <a href="#" id="hero-az" class="hero-cta" style="background:rgba(255,153,0,.15);border-color:rgba(255,153,0,.35);color:#ff9900;display:none" target="_blank" rel="noopener">Amazonで見る →</a>
    </div>"""

# 新: hero-ctasコンテナで横並び
NEW_HERO_RIGHT = """    <div class="hero-right">
      <div class="hero-price" id="hero-price">--</div>
      <div class="hero-ctas">
        <a href="#" id="hero-cta" class="hero-cta" target="_blank" rel="noopener">最安を見る →</a>
        <a href="#" id="hero-az" class="hero-cta hero-cta-az" style="display:none" target="_blank" rel="noopener">Amazon →</a>
      </div>
    </div>"""

html = html.replace(OLD_HERO_RIGHT, NEW_HERO_RIGHT)
print("✅ PATCH 2: Hero CTAボタン構造更新")

# ============================================================
# PATCH 3: Nav をdivで囲む（nav-wrap追加）
# ============================================================

OLD_NAV = """<nav class="nav" aria-label="メインナビゲーション">"""
NEW_NAV = """<div class="nav-wrap">
<nav class="nav" aria-label="メインナビゲーション">"""

html = html.replace(OLD_NAV, NEW_NAV)

# navの閉じタグの後にdivの閉じタグを追加
html = html.replace("</nav>\n\n<main>", "</nav>\n</div>\n\n<main>")
print("✅ PATCH 3: Nav wrapper追加")

# ============================================================
# PATCH 4: データソース表示を「3」に更新
# ============================================================

html = html.replace(
    '<div class="st-v pu">2</div><div class="st-s">楽天 + 公式</div>',
    '<div class="st-v pu">3</div><div class="st-s">楽天 + 公式 + Amazon</div>'
)
print("✅ PATCH 4: データソース 2→3 更新")

# ============================================================
# PATCH 5: renderRank テーブル行のリンク部分にtd-linksコンテナ追加
# ============================================================

# テーブル行のリンク列を <div class="td-links"> で囲む
OLD_LINK_TD = """<td><a href="${r.url||'#'}" target="_blank" rel="noopener" class="cta cta-p" onclick="trackCTA('${r.brand}','${sl}','${r.url}')">${cl} &rarr;</a>${az}</td>"""
NEW_LINK_TD = """<td><div class="td-links"><a href="${r.url||'#'}" target="_blank" rel="noopener" class="cta cta-p" onclick="trackCTA('${r.brand}','${sl}','${r.url}')">${cl} &rarr;</a>${az}</div></td>"""

html = html.replace(OLD_LINK_TD, NEW_LINK_TD)
print("✅ PATCH 5: ランキング行リンクにtd-linksコンテナ追加")

# ============================================================
# PATCH 6: Footer更新
# ============================================================

OLD_FOOTER = """<p>ProteAlert &copy; 2026 &mdash; <a href="https://x.com/ProteAlert" target="_blank" rel="noopener">@ProteAlert</a> &middot; 毎日自動更新 &middot; 楽天 + 公式サイト横断比較</p>"""
NEW_FOOTER = """<p>ProteAlert &copy; 2026 &mdash; <a href="https://x.com/ProteAlert" target="_blank" rel="noopener">@ProteAlert</a> &middot; 毎日自動更新 &middot; 楽天 + 公式 + Amazon 横断比較</p>"""

html = html.replace(OLD_FOOTER, NEW_FOOTER)
print("✅ PATCH 6: Footer更新")

# ============================================================
# PATCH 7: アラートカードのグラデーション線を薄く（::before→opacity .6）
# これはCSS側で既に対応済み（height:2px + opacity:.6）
# ============================================================

# ============================================================
# 書き出し
# ============================================================
with open(FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n🎉 デザインリニューアル完了！")
print(f"   バックアップ: {backup}")
print(f"   変更ファイル: {FILE}")
print(f"\n📋 次のステップ:")
print(f"   1. ブラウザで https://kokusaitomita-blip.github.io/protealert/ を確認")
print(f"   2. git add -A && git commit -m 'Design refinement v2' && git push")
print(f"   3. 問題があれば: copy {backup} {FILE}")
