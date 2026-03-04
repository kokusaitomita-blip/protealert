with open(r'C:\protealert\index.html', 'r', encoding='utf-8') as f:
    h = f.read()
old = 'data-sec="chart">'
idx = h.find(old)
end = h.find('</button>', idx) + len('</button>')
h = h[:end] + '\n  <button data-sec="guide">\U0001f4d6 あれこれ</button>' + h[end:]
with open(r'C:\protealert\index.html', 'w', encoding='utf-8') as f:
    f.write(h)
print('guide count:', h.count('data-sec="guide"'))
