from flask import Flask,session,redirect,url_for,render_template

app = Flask(__name__)
app.secret_key=")H+MbQeThWmZq4t7w!z%C*F-JaNcRfUj"

@app.route("/login/<username>")
def login(username):
    session["username"] = username
    return redirect(url_for ("home"))



    
@app.route("/home")
def home():
    return render_template ("home.html",username = session["username"])


if __name__ == "__main__":
   app.run(debug = True)