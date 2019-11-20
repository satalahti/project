from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hellohello():
    return render_template("hellohello.html")

if __name__ == '__main__':
    app.run(debug=True)
