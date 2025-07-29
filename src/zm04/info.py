# %%
import typer
import feedparser
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()


import urllib.request
import xml.etree.ElementTree as ET

# 表示したいフィード（国内 + 国際）
sources = {
    "NHK": "https://www3.nhk.or.jp/rss/news/cat0.xml",
    "BBC": "http://feeds.bbci.co.uk/news/world/rss.xml",
    'YahooIT': 'https://news.yahoo.co.jp/rss/topics/it.xml',
    'Yahoo経済':'https://news.yahoo.co.jp/rss/topics/business.xml'
}

for name, url in sources.items():
    print(f"\n ◎{name}のニュース")
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            root = ET.fromstring(data)

            items = root.findall(".//item")
            for item in items[:5]:  # 最新5件のみ表示
                title = item.findtext("title", default="タイトルなし")
                print(f" - {title.strip()}")
    except Exception as e:
        print(f"  エラーが発生しました：{e}")

# %%
