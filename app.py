from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<int:id>')
def user(id):
    user = None
    return render_template('user.html', user=user)

app.run(port=5000)
