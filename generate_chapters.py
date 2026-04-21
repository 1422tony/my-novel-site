import os

# 設定範圍
start_chapter = 199
end_chapter = 569

# HTML 模板內容 (使用 f-string 注入變數)
def get_template(current, prev_ch, next_ch):
    # CSS 裡面的大括號 {{ }} 需要雙重寫法以避開 Python 的格式化
    return f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>第 {current} 章 - 小說標題</title>
    <style>
        body {{
            font-family: 'Helvetica Neue', Arial, '微軟正黑體', sans-serif;
            line-height: 1.8;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            background-color: #fff;
            min-height: 100vh;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }}
        .nav-bar {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }}
        .nav-bar.footer {{
            justify-content: center;
            gap: 20px;
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid #eee;
        }}
        .btn {{
            display: inline-block;
            padding: 10px 20px;
            background-color: #eee;
            border-radius: 5px;
            text-decoration: none;
            color: #333;
            transition: 0.2s;
        }}
        .btn:hover {{ background-color: #ddd; }}
        .chapter-title {{ text-align: center; margin-bottom: 30px; }}
        .content {{ font-size: 1.25em; text-align: justify; }}
        .content p {{ margin-bottom: 20px; text-indent: 2em; }}
    </style>
</head>
<body>

<div class="container">
    <div class="nav-bar">
        <a href="index.html" class="btn">返回目錄</a>
    </div>

    <h1 class="chapter-title">第 {current} 章</h1>

    <div class="content">
        <p>這是第 {current} 章的內容預留位置。</p>
        <p>你可以在這裡貼上實際的小說文字...</p>
    </div>

    <div class="nav-bar footer">
        <a href="chapter_{prev_ch}.html" class="btn">上一章</a>
        <a href="chapter_{next_ch}.html" class="btn">下一章</a>
    </div>
</div>

</body>
</html>
"""

def generate():
    print(f"正在生成第 {start_chapter} 到 {end_chapter} 章...")
    
    for i in range(start_chapter, end_chapter + 1):
        file_name = f"chapter_{i}.html"
        prev_ch = i - 1
        next_ch = i + 1
        
        # 寫入檔案
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(get_template(i, prev_ch, next_ch))
            
    print("生成完畢！")

if __name__ == "__main__":
    generate()