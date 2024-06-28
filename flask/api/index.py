from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 用户登录信息
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username in users and users[username] == password:
            # 登录成功,重定向到抢票页面
            return redirect(url_for("ticket"))
        else:
            # 登录失败,显示错误信息
            error = "Invalid username or password"
            return render_template("login.html", error=error)
    
    return render_template("login.html")

@app.route("/ticket")
def ticket():
    # 这里编写抢票页面的逻辑
    return render_template("ticket.html")

if __name__ == "__main__":
    app.run(debug=True)
