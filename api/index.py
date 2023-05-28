import requests
from bs4 import BeautifulSoup
from flask import Flask, request

app = Flask(__name__)

@app.route('/lyric/<t>')
def index(t):
    req = request.args
    artist_name=""
    if req.get("artist_name"):
        artist_name = req.get("artist_name")
    # URLを指定
    url = "https://utaten.com/search?sort=popular_sort_asc&artist_name=&title="+t+"&artist_name="+artist_name  # ご自身のURLに置き換えてください
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    result = soup.find_all("table")
    #print(result[1].find("a").herf)
    url="https://utaten.com/"+result[1].find("a").get('href')
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    div_text = ''
    for element in soup.find_all(class_='rt'):
        element.extract()
    for element in soup.select('div.hiragana'):
        div_text += element.get_text()
    div_text = div_text.replace('<br>', '').replace('<span>spam</span>', '')
    # スペースの除去
    div_text = div_text.replace(' ', '')
    # 結果の表示
    print(div_text)
    return div_text.replace("\n", "<br>")

app.run()