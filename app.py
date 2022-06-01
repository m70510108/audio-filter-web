from flask import Flask, render_template#import類別
app = Flask(__name__)#實體化物件給名稱"app"

@app.route('/')#裝飾器(更目錄、路由)
def home():
    return render_template('AudioHome.html')
@app.route('/intro')
def intro():
    return render_template('AudioIntro.html')
@app.route('/filter')
def filter():
    return render_template('AudioFilter.html')

#app.add_url_rule('/about', 'about', about)#路由、路由名稱、function name
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5078, debug=True, use_reloader = True)
    #debug mode=False 才不會洩漏code中的資料
    #但他不會自動變更望葉，要跳出諸端雞重啟
    #use_reloader = True自動變更

#同步變更1先更新自己在github == git push
#編輯
