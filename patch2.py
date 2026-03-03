with open('index.html','r',encoding='utf-8') as f:
    c=f.read()

# 1. Desktop table: Add Amazon button after existing CTA
old1 = "' + cl + ' &rarr;</a></td></tr>';"
new1 = "' + cl + ' &rarr;</a>' + (r.amazon_url ? ' <a href=\"' + r.amazon_url + '\" target=\"_blank\" rel=\"noopener\" class=\"cta cta-az\" onclick=\"trackEvent(\\'cta_click\\',{brand:\\'' + r.brand + '\\',source:\\'amazon\\',rank:' + (i+1) + '})\">Amazon &rarr;</a>' : '') + '</td></tr>';"
cnt1 = c.count(old1)
c = c.replace(old1, new1, 1)

# 2. Find mobile card CTA pattern
old2 = "' + cl + ' &rarr;</a></div></div>';"
new2 = "' + cl + ' &rarr;</a>' + (r.amazon_url ? ' <a href=\"' + r.amazon_url + '\" target=\"_blank\" rel=\"noopener\" class=\"cta cta-az\" onclick=\"trackEvent(\\'cta_click\\',{brand:\\'' + r.brand + '\\',source:\\'amazon\\'})\">Amazon &rarr;</a>' : '') + '</div></div>';"
cnt2 = c.count(old2)
c = c.replace(old2, new2, 1)

# 3. Alert card: find purchase link pattern
idx = c.find('購入ページ &rarr;</a></div></div>')
cnt3 = 0
if idx > 0:
    old3 = '購入ページ &rarr;</a></div></div>'
    new3 = "購入ページ &rarr;</a>' + (a.amazon_url ? ' <a href=\"' + a.amazon_url + '\" target=\"_blank\" rel=\"noopener\" class=\"cta cta-az\">Amazon &rarr;</a>' : '') + '</div></div>"
    # Need to check exact ending
    snippet = c[idx:idx+100]
    cnt3 = 1

# 4. Hero JS: Add Amazon logic after hero onclick
old4 = "best.url);\n  const us="
if old4 not in c:
    old4 = "best.url);\n  var us="
cnt4 = c.count(old4)
if cnt4 > 0:
    new4 = old4.replace(old4, old4.split('\n')[0] + "\n  var hazl=document.getElementById('hero-az');if(best.amazon_url){hazl.href=best.amazon_url;hazl.style.display='inline-flex';}else{hazl.style.display='none';}\n  " + old4.split('\n')[1])
    c = c.replace(old4, new4, 1)

# 5. Data mapping: Add amazon_url to daily_ranking
old5 = "shop_name: ''"
new5 = "shop_name: '',\n        amazon_url: r.amazon_url || null"
cnt5 = c.count(old5)
c = c.replace(old5, new5, 1)

# 6. Data mapping: Add amazon_url to alerts
old6 = "official_url: a.url"
new6 = "official_url: a.url,\n        amazon_url: a.amazon_url || null"
cnt6 = c.count(old6)
c = c.replace(old6, new6, 1)

with open('index.html','w',encoding='utf-8') as f:
    f.write(c)

print(f'Desktop CTA found: {cnt1}')
print(f'Mobile CTA found: {cnt2}')
print(f'Alert found: {cnt3}')
print(f'Hero JS found: {cnt4}')
print(f'Ranking map: {cnt5}')
print(f'Alert map: {cnt6}')
print(f'cta-az in result: {"cta-az" in c}')
print(f'amazon_url in result: {"amazon_url" in c}')
print(f'Size: {len(c)}')