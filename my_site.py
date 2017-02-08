from flask import Flask, render_template
import requests

app = Flask(__name__)
app.debug = True

def get_data():
    url = "http://api.data.mos.ru/v1/datasets/2462/rows"
    r = requests.get(url)
    return r.json()


@app.route('/')
def list_rows():
    return render_template("list_rows.html",
                           data=get_data())

@app.route('/table/<int:n>')
def show_table(n):
    data = get_data()
    row = data[n]
    return render_template("show_table.html",
                           table=row)

if __name__ == '__main__':
    app.run()