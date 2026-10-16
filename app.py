from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "title": "今天的主子又把水杯打翻了",
        "author": "奴才小明",
        "content": "早上出門前急急忙忙，結果一回家看到客廳滿地水灘，主子還一臉無辜地坐在旁邊舔毛……"
    },
    {
        "title": "第一次帶狗狗去草地奔跑",
        "author": "新手狗爸",
        "content": "今天天氣很好，帶黃金獵犬去大安森林公園。它一看到草地直接瘋掉，拉都拉不住，超可愛！"
    }
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
