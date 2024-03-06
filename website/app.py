from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_main_page():
    return render_template("index.html")

@app.route('/api')
def show_api_page():
    return render_template("api.html")

@app.route('/about')
def show_about_page():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
