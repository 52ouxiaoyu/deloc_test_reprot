import os

REPORT_ROOT = "."  # 当前目录
OUTPUT_FILE = "index.html"

html_header = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Allure Report Index</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        h1 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; }
        a { text-decoration: none; color: #1a73e8; }
    </style>
</head>
<body>
    <h1>Allure 报告列表</h1>
    <ul>
"""

html_footer = """
    </ul>
</body>
</html>
"""

items = []

for entry in os.listdir(REPORT_ROOT):
    path = os.path.join(REPORT_ROOT, entry)
    if os.path.isdir(path):
        index_path = os.path.join(path, "index.html")
        if os.path.isfile(index_path):
            items.append(f'<li><a href="{entry}/index.html">{entry}</a></li>')

with open(os.path.join(REPORT_ROOT, OUTPUT_FILE), "w", encoding="utf-8") as f:
    f.write(html_header)
    f.write("\n".join(sorted(items)))
    f.write(html_footer)

print(f"✅ 已生成 index.html，共发现 {len(items)} 个报告")