from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 設定模板文件夾
app.template_folder = os.path.join(os.path.dirname(__file__), 'templates')

# 靜態文件夾
app.static_folder = os.path.join(os.path.dirname(__file__), 'static')

# 首頁路由
@app.route('/')
def home():
    return render_template('index.html')

# 關於頁面路由
@app.route('/about')
def about():
    return render_template('about.html')

# 聯絡我們頁面路由
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # 在這裡處理提交的數據，例如儲存到數據庫或發送郵件
        return render_template('thank_you.html', name=name)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
