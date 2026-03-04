with open(r'C:\protealert\index.html', 'r', encoding='utf-8') as f:
    h = f.read()
# 2つ目のguideボタンを削除（1つ目だけ残す）
first = h.find('data-sec="guide"')
second = h.find('data-sec="guide"', first + 1)
if second > 0:
    # 2つ目のbutton全体を削除
    start = h.rfind('<button', 0, second)
    end = h.find('</button>', second) + len('</button>')
    h = h[:start] + h[end:]
print('guide count:', h.count('data-sec="guide"'))
with open(r'C:\protealert\index.html', 'w', encoding='utf-8') as f:
    f.write(h)
print('saved')
