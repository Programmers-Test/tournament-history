import datetime
import logging
import logging.handlers
import os
import os.path
import re
import subprocess
import sys


css_styles = """
<head>
  <style>
	body{
		background-color: #f0A51;
	}
  </style>
  <title>Bảng xếp hạng giải đấu</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script async src="https://stats.chessnibble.com/script.js" data-website-id="8205b599-208b-4d50-be05-5a4bb2f3775d"></script>
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
  <link rel="icon" href="https://raw.githubusercontent.com/Thi-Vua-Lay-Tot/Thi-Vua-Lay-Tot.github.io/main/images/favicon.ico" type="image/x-icon" />
  <header>
            <nav>
                <a href="https://thi-vua-lay-tot.github.io/tournaments-leaderboard/">< Quay lại</a>
            </nav>
        </header>
  <style>
    .styled-table {
      font-family: HelveBold;
      border-collapse: collapse;
      width: 100%;
      border: 1px solid #ddd;
      font-size: 16px;
    }
    .styled-table th, .styled-table td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
    .styled-table th {
      background-color: #f0A51;
    }
    body {
      margin-bottom: 70px;
    }
    .github-logo {
      width: 1.5em;
      height: auto;
      vertical-align: middle;
    }
    footer {
      font-family: "Raleway", sans-serif;
      background-color: #04FFf0;
      padding: 5px;
      margin-left: auto;
      margin-top: auto;
      position: fixed;
      bottom: 0;
      right: 0;
      width: 100%;
    }
  </style>
</head>
"""


information = """
  <p><strong>Ghi chú:</strong> Nếu có dấu *?* nghĩa là người chơi này có khả năng không được đạt giải. Nếu có dấu *$* nghĩa là trên lichess.org và dấu *@* tức là trên Chess.com.    </p>
"""
footer_styles = """
<footer>
  <p>
    <a href="https://github.com/Thi-Vua-Lay-Tot/tournaments-leaderboard">
      <img class="github-logo" src="https://github.com/fluidicon.png" alt="GitHub Icon">
    </a>
    Tạo bởi <a href="https://github.com/M-DinhHoangViet">Đinh Hoàng Việt</a>
  </p>
</footer>
"""

def generate_h1_tag(filename):
    title = os.path.splitext(filename)[0].capitalize()
    utc_datetime = datetime.datetime.utcnow()
    h1_tag = f"""<h1 align="center">Bảng xếp hạng {title}<p>
        <i>Lần cuối cập nhật: {utc_datetime.hour}:{utc_datetime.minute}:{utc_datetime.second} UTC, ngày {utc_datetime.day} tháng {utc_datetime.month} năm {utc_datetime.year}</i></p></h1>"""
    return h1_tag

def markdown_table_to_html(markdown_table):
    chesscom = f'https://www.chess.com'
    lichess = f'https://lichess.org'
    rows = markdown_table.strip().split('\n')
    html_table = '<table class="styled-table">\n'
    for i, row in enumerate(rows):
        if '---|---|---|---|---|---|---|---' in row:
            continue

        tag = 'th' if i == 0 else 'td'
        cells = re.split(r'\s*\|\s*', row)

        if len(cells) == 1 and cells[0] == '':
            continue
        
        html_table += '  <tr>\n'
        for cell in cells:
            if cell.startswith('@'):
                username = cell[1:]
                cell_content = f'<{tag}><a href="{chesscom}/member/{username}">{cell}</a></{tag}>'
            elif cell.startswith('$'):
                username = cell[1:]
                cell_content = f'<{tag}><a href="{lichess}/@/{username}">{cell}</a></{tag}>'
            elif cell.startswith('%'):
                link = cell[1:]
                cell_content = f'<{tag}><a href="{lichess}/{link}">Nhấn vào đây!</a></{tag}>'
            elif cell.startswith('/'):
                link = cell[1:]
                cell_content = f'<{tag}><a href="{chesscom}/tournament/live/{link}">Nhấn vào đây!</a></{tag}>'
            else:
                cell_content = f'<{tag}>{cell}</{tag}>'
            html_table += f'    {cell_content}\n'
        html_table += '  </tr>\n'
    html_table += '</table>'
    return html_table

directories = ['leaderboard', 'top']

for directory in directories:
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            with open(os.path.join(directory, filename), 'r') as md_file:
                h1_tag = generate_h1_tag(filename)
                
                markdown_table = md_file.read()
                html_table = markdown_table_to_html(markdown_table)

                styled_html_table = css_styles + h1_tag + html_table + footer_styles

                html_filename = os.path.splitext(filename)[0] + '.html'
                with open(os.path.join(directory, html_filename), 'w') as html_file:
                    html_file.write(styled_html_table)
