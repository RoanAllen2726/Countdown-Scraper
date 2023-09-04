import csv
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    items = []
    categories = []
    with open('data/20_06_2023.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            items.append(row)
            if row[-1] not in categories and row[-1] != "" and row[-1] != "category":
                categories.append(row[-1])
    return render_template('index.html', items=items[1:], categories=categories)


if __name__ == '__main__':
    app.run()
