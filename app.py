from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET",'POST'])
def index():
    return render_template('index.html')


@app.route("/result", methods=["GET",'POST'])
def result():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    return render_template('result.html',name = name,email = email, message = message)

if __name__ == "__main__":
    app.run(debug=True)