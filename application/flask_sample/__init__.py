#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template

#Flaskオブジェクトの生成
app = Flask(__name__)

#「/」もしくは「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

#viewsフォルダ以下のpyファイルをインポート (*複数ある場合は: test1, test2...)
from flask_sample.views import test
