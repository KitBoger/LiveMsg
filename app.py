# Made by KitBoger.

from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': "your_database_url"
})

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        db.reference('/').update({'last_message': message})
        return redirect(request.url)
    else:
        last_message = db.reference('/last_message').get()
        return render_template('index.html', last_message=last_message)

if __name__ == '__main__':
    app.run(debug=True)