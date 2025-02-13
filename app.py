from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Форма</title>
    </head>
    <body>
        <h1>Заповніть форму</h1>
        <form action="/submit" method="POST">
            <label for="name">Ім'я:</label><br>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email"><br><br>
            <label for="message">Повідомлення:</label><br>
            <textarea id="message" name="message"></textarea><br><br>
            <input type="submit" value="Відправити">
        </form>
    </body>
    </html>
    """

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    return redirect(f"/result?name={name}&email={email}&message={message}")

@app.route("/result", methods=["GET"])
def result():
    name = request.args.get("name")
    email = request.args.get("email")
    message = request.args.get("message")
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Результат</title>
    </head>
    <body>
        <h1>Дякуємо за заповнення форми!</h1>
        <p>Ім'я: {name}</p>
        <p>Email: {email}</p>
        <p>Повідомлення: {message}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)