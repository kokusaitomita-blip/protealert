with open('index.html','r',encoding='utf-8') as f:
    c=f.read()

# 1. Alert card: Add Amazon button
old1 = "楽天で見る &rarr;</a></div></div>';"
new1 = "楽天で見る &rarr;</a>' + (a.amazon_url ? ' <a href=\"' + a.amazon_url + '\" target=\"_blank\" rel=\"noopener\" class=\"cta cta-az\">Amazon &rarr;</a>' : '') + '</div></div>';"
cnt1 = c.count(old1)
c = c.replace(old1, new1, 1)

# 2. Hero: Find renderHero function and add amazon logic
old2 = "function renderHero()"
idx2 = c.find(old2)
# Find the hero-cta href assignment
idx3 = c.find('hero-cta', idx2) if idx2 > 0 else -1
# Find the next function after renderHero
idx4 = c.find('\nfunction ', idx2+1) if idx2 > 0 else -1
hero_block = c[idx2:idx4] if idx2 > 0 and idx4 > 0 else ''
cnt2 = 1 if hero_block else 0

# Find the last line before closing brace
if hero_block:
    # Find end of renderHero - look for closing brace + newline
    last_brace = hero_block.rfind('}')
    if last_brace > 0:
        inject = "  var hazl=document.getElementById('hero-az');if(D.daily_ranking[0].amazon_url){hazl.href=D.daily_ranking[0].amazon_url;hazl.style.display='inline-flex';}else{hazl.style.display='none';}\n"
        insert_pos = idx2 + last_brace
        c = c[:insert_pos] + inject + c[insert_pos:]

with open('index.html','w',encoding='utf-8') as f:
    f.write(c)

print(f'Alert patched: {cnt1}')
print(f'Hero function found: {cnt2}')
print(f'amazon in alerts: {"a.amazon_url" in c}')
print(f'hero-az JS: {"hazl" in c}')