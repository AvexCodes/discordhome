from flask import Flask, request, render_template, redirect, session, make_response
from misc.oauth import Oauth
from misc import jsonHandler as jh
from misc import inject
from db import dbHandler as DataBase

inject.injectVariables()

from routes.errors import router as errRoute

app = Flask(__name__)

app.register_blueprint(errRoute, url_prefix="/errors")

dev = jh.read_json("mode.json")
dev = dev['dev']
@app.route("/", methods=["get"])
def index():
    return "In developement > Login <a href=\"/login\">here</a>"

@app.route("/login", methods=["get"])
def login():
    if "oauth" in request.cookies:
        # magic
        return redirect('/account')
    else:
        if dev == True:
            return redirect(Oauth.discord_login_url_dev)
        else:
            return redirect(Oauth.discord_login_url)
        

@app.route("/auth", methods=["get"])
def auth():
    if request.args.get("code") is None:
        return redirect('/login')
    else:
        code = request.args.get("code")
        if "oauth" in request.cookies:
            return redirect('/account')
        else:
            if code == "":
                return redirect('/login')
            else:

                access_token = Oauth.get_access_token(code)
                if access_token == "invalid code":
                    return redirect('/login')
                else:
                    resp = make_response(redirect("/account"))
                    resp.set_cookie('oauth', access_token, max_age=60*60*24*7)
                    return resp

@app.route("/account", methods=["get"])
def account():
    if "oauth" in request.cookies:
        # magic
        db = DataBase.connect()

        c = db.cursor()
        data = Oauth.get_user_object(request.cookies.get('oauth'))
        c.execute(f"SELECT * FROM userSettings WHERE discordId = '{data['id']}' ")
        userData = c.fetchone()

        print(userData[3])
        return render_template('views/account.html', name=data['username'], avatar=data['id'] + "/" + data['avatar'], cmdTotal=userData[3], earnt=600, last_command=userData[4], bio=userData[2])
    else:
        return redirect('/login')

if __name__ == "__main__":
    if dev == True:
        app.run(debug=True,port=int("5000"))
    else:
        app.run(debug=True,port=int("80"))