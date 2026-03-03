import re
with open('index.html','r',encoding='utf-8') as f:
    c=f.read()

# 1. CSS: Add Amazon button style
old_css='.cta-p{background:rgba(0,212,255,.1);border-color:rgba(0,212,255,.3);color:var(--cyan)}'
new_css=old_css+'\n.cta-az{background:rgba(255,153,0,.12);border-color:rgba(255,153,0,.35);color:#ff9900}\n.cta-az:hover{background:rgba(255,153,0,.22);border-color:#ff9900;color:#ffb844}'
c=c.replace(old_css,new_css)

# 2. Desktop table: Add Amazon link
old_dt='</a></td></tr>`;'
new_dt='</a>${r.amazon_url?` <a href="${r.amazon_url}" target="_blank" rel="noopener" class="cta cta-az" onclick="trackCTA(\'${r.brand}\',\'amazon\',\'${r.amazon_url}\')">Amazon &rarr;</a>`:\'\'}</td></tr>`;'
c=c.replace(old_dt,new_dt,1)

# 3. Mobile card: Add Amazon link
old_mc='</a></div></div>`;'
new_mc='</a>${r.amazon_url?` <a href="${r.amazon_url}" target="_blank" rel="noopener" class="cta cta-az" onclick="trackCTA(\'${r.brand}\',\'amazon\',\'${r.amazon_url}\')">Amazon &rarr;</a>`:\'\'}</div></div>`;'
c=c.replace(old_mc,new_mc,1)

# 4. Alert card: Add Amazon link
old_al="trackCTA('${a.brand}','alert','${a.url}')\">"+chr(36)+'{tl2} &rarr;</a></div></div>`;'
# Simpler approach - find the alert CTA
old_al2='onclick="trackCTA(\'${a.brand}\',\'alert\',\'${a.url}\')">'+u'\u8cfc\u5165\u30da\u30fc\u30b8 &rarr;</a></div></div>`;'
new_al2='onclick="trackCTA(\'${a.brand}\',\'alert\',\'${a.url}\')">'+u'\u8cfc\u5165\u30da\u30fc\u30b8 &rarr;</a>${a.amazon_url?` <a href="${a.amazon_url}" target="_blank" rel="noopener" class="cta cta-az" onclick="trackCTA(\'${a.brand}\',\'amazon\',\'${a.amazon_url}\')">Amazon &rarr;</a>`:\'\'}</div></div>`;'
c=c.replace(old_al2,new_al2,1)

# 5. Hero: Add Amazon button HTML
old_hero='<a href="#" id="hero-cta" class="hero-cta" target="_blank" rel="noopener">'
new_hero=old_hero
old_hero_after='</a>\n    </div>'
# Find and add hero amazon button
hero_btn='<a href="#" id="hero-cta" class="hero-cta" target="_blank" rel="noopener">'
hero_insert_after=hero_btn.split('<a')[0]
c=c.replace(
    'id="hero-cta" class="hero-cta" target="_blank" rel="noopener">',
    'id="hero-cta" class="hero-cta" target="_blank" rel="noopener">',1)

# Actually insert hero Amazon button after hero-cta link
idx=c.find('id="hero-cta"')
if idx>0:
    end_a=c.find('</a>',idx)
    insert_pos=end_a+4
    hero_az='\n      <a href="#" id="hero-az" class="hero-cta" style="background:rgba(255,153,0,.15);border-color:rgba(255,153,0,.35);color:#ff9900;display:none" target="_blank" rel="noopener">Amazonで見る →</a>'
    c=c[:insert_pos]+hero_az+c[insert_pos:]

# 6. Hero JS: Add Amazon logic
old_js="hl.onclick=()=>trackCTA(best.brand,'hero_'+sl,best.url);\n  const us="
new_js="hl.onclick=()=>trackCTA(best.brand,'hero_'+sl,best.url);\n  const hazl=document.getElementById('hero-az');if(best.amazon_url){hazl.href=best.amazon_url;hazl.style.display='inline-flex';hazl.onclick=()=>trackCTA(best.brand,'hero_amazon',best.amazon_url);}else{hazl.style.display='none';}\n  const us="
c=c.replace(old_js,new_js,1)

with open('index.html','w',encoding='utf-8') as f:
    f.write(c)

# Verify
checks=['cta-az','hero-az','amazon_url','hero_amazon']
for ch in checks:
    print(f'{ch}: {ch in c}')
print(f'Total size: {len(c)}')