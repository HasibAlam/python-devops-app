# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# In-memory storage for names (guestbook entries)
guestbook = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        if name:
            guestbook.append(name)
    return render_template('index.html', guestbook=guestbook)

if __name__ == '__main__':
    app.run(debug=True)
