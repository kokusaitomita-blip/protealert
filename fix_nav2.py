with open(r'C:\protealert\index.html', 'r', encoding='utf-8') as f:
    h = f.read()
# 全guideボタンを削除
import re
h = re.sub(r'\s*<button data-sec="guide">.*?</button>', '', h)
# 1つだけ追加
old = '&#x1F4C8; \u4fa1\u683c\u63a8\u79fb</button>\n</nav>'
new = '&#x1F4C8; \u4fa1\u683c\u63a8\u79fb</button>\n  <button data-sec="guide">\U0001f4d6 \u3042\u308c\u3053\u308c</button>\n</nav>'
h = h.replace(old, new, 1)
print('guide count:', h.count('data-sec="guide"'))
with open(r'C:\protealert\index.html', 'w', encoding='utf-8') as f:
    f.write(h)
print('saved')
