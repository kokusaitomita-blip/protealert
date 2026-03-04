"""
ProteAlert 「プロテインあれこれ」タブ追加パッチ
================================================
VPS上で実行: python patch_guide.py

追加内容:
1. Nav に「📖 あれこれ」タブ追加
2. CSS にガイド用スタイル追加
3. <main> 内に sec-guide セクション追加（6セクション）
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

# ============================================================
# PATCH 1: Nav にタブ追加
# ============================================================

html = html.replace(
    '<button data-sec="chart">📈 価格推移</button>',
    '<button data-sec="chart">📈 価格推移</button>\n  <button data-sec="guide">📖 あれこれ</button>'
)
print("✅ PATCH 1: Nav タブ追加")

# ============================================================
# PATCH 2: CSS にガイド用スタイル追加（</style> の直前）
# ============================================================

GUIDE_CSS = """
/* Guide */
.guide{max-width:800px}
.guide-nav{display:flex;gap:.3rem;margin-bottom:1.5rem;flex-wrap:wrap}
.guide-nav button{padding:.4rem .8rem;border:1px solid var(--border);border-radius:20px;background:transparent;color:var(--t2);font-family:inherit;font-size:.72rem;font-weight:500;cursor:pointer;transition:all var(--transition)}
.guide-nav button:hover{border-color:rgba(0,212,255,.3);color:var(--cyan)}
.guide-nav button.active{background:var(--cyan-dim);border-color:rgba(0,212,255,.35);color:var(--cyan)}
.guide-sec{display:none}.guide-sec.active{display:block}
.guide-sec h3{font-size:1rem;font-weight:700;margin:1.5rem 0 .6rem;padding-bottom:.4rem;border-bottom:1px solid var(--border);color:var(--cyan)}
.guide-sec h3:first-child{margin-top:0}
.guide-sec h4{font-size:.88rem;font-weight:700;margin:1.2rem 0 .4rem;color:var(--t1)}
.guide-sec p{font-size:.82rem;color:var(--t1);margin-bottom:.7rem;line-height:1.75}
.guide-sec strong{color:var(--green)}
.guide-table{width:100%;border-collapse:collapse;margin:.8rem 0 1rem;font-size:.78rem}
.guide-table th{background:var(--bg-surface);color:var(--cyan);font-weight:600;padding:.5rem .7rem;text-align:left;border-bottom:1px solid var(--border);white-space:nowrap}
.guide-table td{padding:.5rem .7rem;border-bottom:1px solid var(--border);color:var(--t1);vertical-align:top}
.guide-table tr:hover td{background:rgba(255,255,255,.02)}
.tip-box{background:var(--bg-card);border:1px solid var(--border);border-left:3px solid var(--cyan);border-radius:0 var(--r-sm) var(--r-sm) 0;padding:.8rem 1rem;margin:.8rem 0;font-size:.8rem;color:var(--t1);line-height:1.7}
.tip-box.warn{border-left-color:var(--amber)}
.tip-box .tip-label{font-size:.68rem;font-weight:600;color:var(--cyan);text-transform:uppercase;letter-spacing:.5px;margin-bottom:.3rem}
.tip-box.warn .tip-label{color:var(--amber)}
.evidence{font-size:.72rem;color:var(--t3);margin-top:-.2rem;margin-bottom:.8rem;font-style:italic}
.guide-toc{list-style:none;padding:0;margin:0 0 1.5rem}
.guide-toc li{font-size:.8rem;padding:.3rem 0;color:var(--t2)}
.guide-toc li::before{content:'→ ';color:var(--cyan)}
@media(max-width:768px){
  .guide-table{font-size:.72rem}
  .guide-table th,.guide-table td{padding:.4rem .5rem}
  .guide-nav{gap:.25rem}
  .guide-nav button{font-size:.68rem;padding:.35rem .6rem}
}
"""

html = html.replace("</style>", GUIDE_CSS + "</style>")
print("✅ PATCH 2: ガイド用CSS追加")

# ============================================================
# PATCH 3: guide セクション HTML追加（</main> の直前）
# ============================================================

GUIDE_HTML = """
  <section id="sec-guide" class="sec" aria-labelledby="h-guide">
    <h2 id="h-guide">📖 プロテインあれこれ</h2>

    <nav class="guide-nav" aria-label="ガイド内ナビ">
      <button class="active" data-gsec="faq">よくある疑問</button>
      <button data-gsec="choose">選び方</button>
      <button data-gsec="cospa">コスパ術</button>
      <button data-gsec="howto">飲み方・摂取量</button>
      <button data-gsec="deep">マニアック知識</button>
      <button data-gsec="brands">ブランド早見表</button>
    </nav>

    <!-- ① よくある疑問 -->
    <div id="gsec-faq" class="guide-sec active">
      <h3>よくある疑問</h3>

      <h4>🏋️ プロテイン飲んだらマッチョになる？</h4>
      <p><strong>なりません。</strong>プロテインはただのタンパク質です。筋肉を大きくするには、十分な負荷のトレーニング＋適切な栄養＋休養の3つが必要。プロテインだけ飲んでも筋肉は勝手につきません。逆に、トレーニングしている人にとっては食事だけで必要量を摂るのが大変なので、プロテインは「効率的にタンパク質を補う手段」として優秀です。</p>

      <h4>🍔 プロテインで太る？</h4>
      <p><strong>カロリー収支次第です。</strong>プロテインパウダー1杯（約30g）は約120kcal。これを食事に「追加」すれば当然カロリーは増えますが、甘い間食をプロテインに置き換えるなら逆にカロリーダウンになることが多いです。タンパク質は満腹感を高める効果もあるので、うまく使えばダイエットの味方です。</p>
      <div class="tip-box">
        <div class="tip-label">💡 ポイント</div>
        太る・太らないを決めるのは「1日の総摂取カロリー vs 消費カロリー」のバランス。プロテイン自体は低脂質で高タンパクなので、食事全体のPFCバランスを整えるのに便利です。
      </div>

      <h4>🧪 人工甘味料が入ってるけど大丈夫？</h4>
      <p>プロテインによく使われるのは<strong>アスパルテーム、スクラロース、アセスルファムK</strong>の3つ。結論から言うと、通常の摂取量であれば安全性に大きな問題はありません。</p>
      <table class="guide-table">
        <thead><tr><th>甘味料</th><th>甘さ</th><th>カロリー</th><th>備考</th></tr></thead>
        <tbody>
          <tr><td>アスパルテーム</td><td>砂糖の200倍</td><td>4kcal/g（微量使用）</td><td>IARC発がん性グループ2B（「可能性あり」レベル）</td></tr>
          <tr><td>スクラロース</td><td>砂糖の600倍</td><td>0kcal</td><td>体内でほぼ吸収されず排出</td></tr>
          <tr><td>アセスルファムK</td><td>砂糖の200倍</td><td>0kcal</td><td>ADI（1日許容量）に基づく使用基準あり</td></tr>
        </tbody>
      </table>
      <p>IARCの「グループ2B」は「発がん性の可能性がある」というカテゴリーで、同じ分類にはアロエベラ抽出物や漬物も含まれます。JECFAが設定したアスパルテームのADI（体重1kgあたり40mg）を超えるには、体重70kgの人で清涼飲料水9〜14本を毎日飲む計算になります。</p>
      <div class="tip-box warn">
        <div class="tip-label">⚠️ ただし注意</div>
        WHOは2023年のガイドラインで「減量目的での人工甘味料の長期使用は推奨しない」と勧告しています。気になる人はノンフレーバー（甘味料不使用）のプロテインを選ぶ手もあります。SAVEやALPRONなどにはノンフレーバータイプがあります。
      </div>

      <h4>🥄 ダマになりにくくするには？</h4>
      <p>ダマの原因は「粉を液体に入れる順番」と「温度」です。</p>
      <table class="guide-table">
        <thead><tr><th>コツ</th><th>理由</th></tr></thead>
        <tbody>
          <tr><td><strong>水を先に入れる</strong></td><td>粉が底に固まらず分散しやすい</td></tr>
          <tr><td><strong>常温〜冷水を使う</strong></td><td>熱湯だとタンパク質が変性してダマになる</td></tr>
          <tr><td><strong>シェイカーを使う</strong></td><td>スプーンで混ぜるだけでは不十分。20〜30回振る</td></tr>
          <tr><td><strong>WPIを選ぶ</strong></td><td>WPCより溶けやすい傾向がある</td></tr>
        </tbody>
      </table>

      <h4>🥤 プロテインシェイカーの選び方</h4>
      <p>シェイカーの違いは「混ざりやすさ」「容量」「洗いやすさ」の3点で決まります。</p>
      <table class="guide-table">
        <thead><tr><th>タイプ</th><th>特徴</th><th>おすすめ度</th></tr></thead>
        <tbody>
          <tr><td>ブレンダーボール付き</td><td>バネ状のボールで撹拌力が高い。ダマになりにくい</td><td>★★★</td></tr>
          <tr><td>メッシュ付き</td><td>フタ裏にメッシュフィルター。ダマを物理的にカット</td><td>★★★</td></tr>
          <tr><td>シンプルタイプ</td><td>安価だが混ざりは劣る。しっかり振れば問題なし</td><td>★★</td></tr>
          <tr><td>電動シェイカー</td><td>ボタン一つで完璧に混ざる。洗い物がやや面倒</td><td>★★（好み次第）</td></tr>
        </tbody>
      </table>
      <div class="tip-box">
        <div class="tip-label">💡 実用Tips</div>
        容量は500ml以上が使いやすい（水200ml+粉+振るスペース）。広口タイプは粉を入れやすく洗いやすい。パッキンが外れるタイプは衛生的。ジム用なら漏れ防止ロック付きが安心。
      </div>
    </div>

    <!-- ② 選び方ガイド -->
    <div id="gsec-choose" class="guide-sec">
      <h3>プロテインの選び方</h3>

      <h4>種類の違い</h4>
      <table class="guide-table">
        <thead><tr><th>種類</th><th>原料</th><th>タンパク質含有率</th><th>吸収速度</th><th>コスト</th><th>向いている人</th></tr></thead>
        <tbody>
          <tr><td><strong>WPC</strong></td><td>ホエイ（乳清）</td><td>70〜80%</td><td>速い（1〜2時間）</td><td>安い</td><td>コスパ重視の人</td></tr>
          <tr><td><strong>WPI</strong></td><td>ホエイ（乳清）</td><td>85〜95%</td><td>速い</td><td>中〜高</td><td>乳糖不耐症・脂質を控えたい人</td></tr>
          <tr><td><strong>WPH</strong></td><td>ホエイ（加水分解）</td><td>80〜90%</td><td>最速</td><td>高い</td><td>消化吸収を最大化したい人</td></tr>
          <tr><td><strong>カゼイン</strong></td><td>牛乳</td><td>80〜85%</td><td>遅い（6〜8時間）</td><td>中</td><td>就寝前の摂取に</td></tr>
          <tr><td><strong>ソイ</strong></td><td>大豆</td><td>80〜90%</td><td>中程度</td><td>安い</td><td>乳製品を避けたい人・ヴィーガン</td></tr>
        </tbody>
      </table>

      <h4>結局どれを買えばいい？</h4>
      <p>迷ったら<strong>WPC</strong>でOK。コスパが最も良く、大半のトレーニーはこれで十分です。牛乳でお腹がゴロゴロする人は<strong>WPI</strong>を。就寝前に飲むなら<strong>カゼイン</strong>がベスト。植物性が良ければ<strong>ソイ</strong>。</p>
      <div class="tip-box">
        <div class="tip-label">💡 WPCとWPIの価格差</div>
        WPIはWPCより1.3〜1.5倍ほど高い傾向がありますが、タンパク質含有率が高い分、g単価で見ると差が縮まることもあります。ProteAlertのランキングでg単価を比較してみてください。
      </div>
    </div>

    <!-- ③ コスパ術 -->
    <div id="gsec-cospa" class="guide-sec">
      <h3>コスパ最強の買い方</h3>

      <h4>g単価で判断する</h4>
      <p>プロテインの「安さ」を比べるなら、<strong>商品価格ではなくg単価（1gあたりの価格）</strong>で見るのが鉄則。3kgで6,000円の商品と1kgで2,500円の商品、g単価で見ると2.0円/g vs 2.5円/g で前者の方がお得です。ProteAlertはこの計算を全商品に対して自動で行っています。</p>

      <h4>容量別の傾向</h4>
      <table class="guide-table">
        <thead><tr><th>容量</th><th>g単価傾向</th><th>こんな人向け</th></tr></thead>
        <tbody>
          <tr><td>750g〜1kg</td><td>割高</td><td>味を試したい・初めて買う人</td></tr>
          <tr><td>3kg</td><td>コスパ良好</td><td>定番のサイズ。多くのブランドで最安帯</td></tr>
          <tr><td>5kg</td><td>最安になることが多い</td><td>味が決まっている人・消費量が多い人</td></tr>
        </tbody>
      </table>

      <h4>楽天 vs Amazon vs 公式の使い分け</h4>
      <table class="guide-table">
        <thead><tr><th>ストア</th><th>メリット</th><th>デメリット</th></tr></thead>
        <tbody>
          <tr><td><strong>楽天</strong></td><td>ポイント還元が大きい（お買い物マラソン・SPU）</td><td>ポイント計算が複雑</td></tr>
          <tr><td><strong>Amazon</strong></td><td>配送が速い。定期おトク便で割引</td><td>ポイント還元は控えめ</td></tr>
          <tr><td><strong>公式サイト</strong></td><td>限定セール・初回割引が強い（特にマイプロ、Be Legend）</td><td>送料がかかる場合あり</td></tr>
        </tbody>
      </table>
      <div class="tip-box">
        <div class="tip-label">💡 実践テクニック</div>
        楽天のお買い物マラソン時にまとめ買いが最強パターン。SPU倍率を上げた状態で、5のつく日にエントリーして購入すると10%以上還元も狙えます。Amazonは定期おトク便（最大15%OFF）が安定。公式はフラッシュセールを狙い撃ち。
      </div>
    </div>

    <!-- ④ 飲み方・摂取量 -->
    <div id="gsec-howto" class="guide-sec">
      <h3>飲み方・タイミング・摂取量</h3>

      <h4>1日にどれくらい摂ればいい？</h4>
      <table class="guide-table">
        <thead><tr><th>目的</th><th>体重1kgあたり</th><th>体重70kgの場合</th></tr></thead>
        <tbody>
          <tr><td>一般的な健康維持</td><td>0.8〜1.0g</td><td>56〜70g</td></tr>
          <tr><td>筋トレ＋筋肥大</td><td>1.6〜2.2g</td><td>112〜154g</td></tr>
          <tr><td>ダイエット中（筋量維持）</td><td>1.6〜2.4g</td><td>112〜168g</td></tr>
        </tbody>
      </table>
      <p class="evidence">参考: ISSN（国際スポーツ栄養学会）ポジションスタンド / Stokes et al. (2018) Nutrients</p>

      <h4>1回の摂取量</h4>
      <p><strong>1回20〜40g</strong>が目安。これを<strong>3〜4回に分散</strong>して摂ると、筋タンパク質合成（MPS）を効率よく刺激できます。1回に大量に摂っても、余った分は筋合成に使われず酸化されてしまいます。</p>

      <h4>ゴールデンタイム（30分以内）は神話？</h4>
      <p>「トレーニング後30分以内にプロテインを飲まないと効果がない」というのは<strong>科学的には否定されています。</strong></p>
      <p>複数のメタ分析の結論は一貫しています：</p>
      <div class="tip-box">
        <div class="tip-label">📊 エビデンス</div>
        アナボリックウィンドウ（同化の窓）は、一般に言われる30〜60分ではなく<strong>4〜6時間</strong>程度と考えられています。そもそも1日のトータルのタンパク質摂取量の方がはるかに重要で、タイミングの効果があるとしても「比較的小さい」とされています。<br>
        ただし、空腹状態でトレーニングした場合は、運動後早めに摂取した方が良いとされています。
      </div>
      <p class="evidence">参考: Schoenfeld et al. (2013) JISSN / Aragon & Schoenfeld (2013) JISSN / Casuso & Goossens (2025) Nutrients</p>

      <h4>おすすめの飲み方パターン</h4>
      <table class="guide-table">
        <thead><tr><th>タイミング</th><th>量</th><th>ポイント</th></tr></thead>
        <tbody>
          <tr><td>朝食時</td><td>20〜30g</td><td>就寝中の絶食状態をリセット</td></tr>
          <tr><td>トレーニング前後</td><td>20〜40g</td><td>前後2〜3時間以内でOK</td></tr>
          <tr><td>間食（午後）</td><td>20〜30g</td><td>食事間のMPS維持に</td></tr>
          <tr><td>就寝前</td><td>30〜40g</td><td>カゼインがベスト（ゆっくり吸収）</td></tr>
        </tbody>
      </table>
    </div>

    <!-- ⑤ マニアック知識 -->
    <div id="gsec-deep" class="guide-sec">
      <h3>マニアック知識（エビデンス付き）</h3>

      <h4>🔬 ホエイ × 運動で悪玉コレステロールが下がる</h4>
      <p>2024年のメタ分析（21のRCTを統合）によると、ホエイプロテインの摂取と運動を組み合わせた群で、<strong>LDLコレステロール（悪玉）</strong>と<strong>総コレステロール</strong>の有意な低下が確認されています。特に50歳未満・BMI 25以上の層で効果が顕著でした。12週間以上の摂取で中性脂肪の低下も報告されています。</p>
      <p class="evidence">参考: Clinical Nutrition (2024) - Whey protein supplementation and cardiometabolic health: meta-analysis of 21 RCTs</p>

      <h4>🧬 ロイシンとmTORC1</h4>
      <p>ホエイプロテインが筋合成に特に有効な理由は、<strong>ロイシン（BCAA）の含有量が多い</strong>こと。ロイシンは筋細胞内のmTORC1（タンパク質合成のマスタースイッチ）を直接活性化します。ホエイの加水分解物（WPH）は、少量でもロイシンの筋肉への取り込みを増やし、mTORC1を効率的に活性化することが示されています。</p>
      <p class="evidence">参考: Moro et al. (2019) The Journal of Nutrition - WPH crossover trial</p>

      <h4>🌙 就寝前カゼインで夜間のMPSが上がる</h4>
      <p>就寝前に摂取したカゼインプロテインは、睡眠中にしっかり消化・吸収され、<strong>夜間の筋タンパク質合成率を上昇</strong>させることが確認されています。ホエイは吸収が速すぎて夜間をカバーしきれないため、就寝前にはカゼイン（またはカゼインブレンド）が推奨されています。</p>
      <p class="evidence">参考: Snijders et al. - Pre-sleep protein and muscle adaptation</p>

      <h4>🌅 朝のタンパク質比率と筋量の関係</h4>
      <p>ある研究では、<strong>1日のタンパク質摂取量のうち朝食の比率が高い人ほど、筋量と握力が良好</strong>だったと報告されています。朝はMPSの感受性が高い可能性があり、朝食でしっかりタンパク質を摂ることが推奨されます。日本人は朝のタンパク質が不足しがちなので、朝プロテイン1杯を習慣にするだけで改善できます。</p>
      <p class="evidence">参考: Lak et al. (2024) Frontiers in Nutrition</p>

      <h4>👴 高齢者こそホエイプロテイン</h4>
      <p>2025年のメタ分析（高齢者対象）では、ホエイプロテインの摂取が<strong>除脂肪体重と筋力の改善</strong>に有効であることが示されています。特にレジスタンストレーニングと組み合わせた場合に効果が大きくなります。サルコペニア（加齢による筋肉減少）の予防にも重要です。</p>
      <p class="evidence">参考: Khalafi et al. (2025) Healthcare - Whey protein in older adults: meta-analysis</p>

      <h4>🥛 ホエイ+食物繊維で血糖コントロール改善</h4>
      <p>ホエイプロテインと食物繊維を組み合わせると、ホエイ単体やカーボ単体よりも<strong>血糖コントロールが改善</strong>されるという系統的レビューがあります。プロテインを飲む際にオートミールや野菜と一緒に摂ると、血糖値の急上昇を抑えつつ筋合成もサポートできます。</p>
      <p class="evidence">参考: Applied Sciences (2025) - Whey protein, carbohydrate, and fibre: systematic review</p>
    </div>

    <!-- ⑥ ブランド早見表 -->
    <div id="gsec-brands" class="guide-sec">
      <h3>国内主要ブランド早見表</h3>

      <table class="guide-table">
        <thead><tr><th>ブランド</th><th>主な種類</th><th>特徴</th><th>価格帯</th></tr></thead>
        <tbody>
          <tr><td><strong>SAVE</strong></td><td>WPC</td><td>国内最安クラスのg単価。ノンフレーバーあり。大容量（5kg）が強い</td><td>安い</td></tr>
          <tr><td><strong>ALPRON</strong></td><td>WPC / WPI</td><td>国産メーカー。フレーバー豊富。品質安定</td><td>安い〜中</td></tr>
          <tr><td><strong>エクスプロージョン</strong></td><td>WPC</td><td>3kgの大容量コスパ型。セールが頻繁</td><td>安い</td></tr>
          <tr><td><strong>マイプロテイン</strong></td><td>WPC / WPI / カゼイン</td><td>世界最大手。ゾロ目セール・フラッシュセールが強力。フレーバー60種以上</td><td>セール時安い</td></tr>
          <tr><td><strong>REYS</strong></td><td>WPC</td><td>山澤礼明プロデュース。1kgサイズが主力。味の評価が高い</td><td>中</td></tr>
          <tr><td><strong>Be Legend</strong></td><td>WPC / WPI</td><td>国内製造。コラボフレーバーが話題。公式サイトのセールが強い</td><td>中</td></tr>
          <tr><td><strong>バルクス</strong></td><td>WPC / WPI</td><td>山本義徳監修。高品質路線。フレーバーの完成度が高い</td><td>中〜高</td></tr>
          <tr><td><strong>DNS</strong></td><td>WPC / WPI</td><td>国内老舗。ジムでの取り扱い多。品質は安定だがやや割高</td><td>高い</td></tr>
          <tr><td><strong>ザバス</strong></td><td>WPC / ソイ</td><td>明治ブランドの安心感。コンビニで買える手軽さ。g単価は高め</td><td>高い</td></tr>
          <tr><td><strong>ゴールドスタンダード</strong></td><td>WPI / WPC</td><td>世界的定番。WPIメインで高品質。海外からの購入がコスパ良</td><td>中〜高</td></tr>
        </tbody>
      </table>
      <div class="tip-box">
        <div class="tip-label">💡 ブランド選びのコツ</div>
        ブランドの知名度や評判よりも、<strong>g単価とタンパク質含有率</strong>で比較するのが合理的。ProteAlertのランキングで最新のg単価を毎日チェックできます。高いブランド=高品質とは限りません。
      </div>
    </div>

  </section>
"""

html = html.replace("</main>", GUIDE_HTML + "</main>")
print("✅ PATCH 3: ガイドセクションHTML追加")

# ============================================================
# PATCH 4: ガイド内ナビのJS追加（既存navのJSの後に追加）
# ============================================================

GUIDE_JS = """
// Guide sub-nav
document.querySelectorAll('.guide-nav button').forEach(b=>{b.addEventListener('click',()=>{document.querySelectorAll('.guide-nav button').forEach(x=>x.classList.remove('active'));document.querySelectorAll('.guide-sec').forEach(x=>x.classList.remove('active'));b.classList.add('active');document.getElementById('gsec-'+b.dataset.gsec).classList.add('active');});});
"""

# 既存のnav JSの後に追加
html = html.replace(
    "if(b.dataset.sec==='chart'&&!chartInst)loadChart();});});",
    "if(b.dataset.sec==='chart'&&!chartInst)loadChart();});\n});\n" + GUIDE_JS
)

# 上の置換で }); が重複しないよう修正（元コードの閉じを消す）
# 実際には元コードが });});  なので片方を消費済み
print("✅ PATCH 4: ガイド内ナビJS追加")

# ============================================================
# 書き出し
# ============================================================
with open(FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n🎉 「プロテインあれこれ」タブ追加完了！")
print(f'git add -A && git commit -m "Add protein guide tab" && git push')
