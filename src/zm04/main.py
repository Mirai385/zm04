import datetime
import feedparser
import typer
import urllib.request
import xml.etree.ElementTree as ET


from . import mathtools
from . import demo
app = typer.Typer()


@app.callback()
def callback():
    """
    A Collection of Useful Commands
    """


@app.command()
def now():
    """
    Show local date and time
    """
    today = datetime.datetime.today()
    typer.echo(today.strftime('%A, %B %d, %Y'))


@app.command()
def gcd(x: int, y: int):
    """
    Greatest Common Divisor
    """
    typer.echo(mathtools.gcd(x, y))

@app.command()
def lcm(x:int, y:int):
    typer.echo(mathtools.lcm(x, y))

@app.command()
def divisors(m:int):
    typer.echo(mathtools.divisors(m))

@app.command()
def is_prime(m:int):
    typer.echo(mathtools.is_prime(m))

@app.command()
def hello(name: str = "Mirai"):
    typer.echo(demo.hello,{name})

@app.command()
def info():
    sources = {
        "NHK": "https://www3.nhk.or.jp/rss/news/cat0.xml",
        "BBC": "http://feeds.bbci.co.uk/news/world/rss.xml",
        "YahooIT": "https://news.yahoo.co.jp/rss/topics/it.xml",
        "Yahoo経済": "https://news.yahoo.co.jp/rss/topics/business.xml"
    }

    for name, url in sources.items():
        print("=" * 50)
        print(f"\n◎ {name} のニュース")
        print("-" * 50)
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read()
                root = ET.fromstring(data)

                items = root.findall(".//item")
                for item in items[:5]:  # 最新5件のみ表示
                    title = item.findtext("title", default="タイトルなし").strip()
                    link = item.findtext("link", default="リンクなし").strip()
                    print(f" - {title}\n   {link}")
        except Exception as e:
            print(f"  エラーが発生しました：{e}")




   


