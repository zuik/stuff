import flask as f
import redis
import time
import re
import logging
from logging.handlers import RotatingFileHandler
import hashlib
'''
Todo list:
 - User
 - Authentication
 - Time zone
 - Pages
 - Like button, are we making Facebook?
 - Streaming, are we making Twitter?
 - API
 - CLI client

'''



app = f.Flask(__name__)
r = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route("/")
def index():
    count_id = int(r.get("msg:id").decode())
    if count_id == 0:
        return f.render_template("index.html", msg=[])
    else:
        return f.render_template("index.html", msg=_get_msg(count_id))

def _get_msg(count):
    messages = []
    for i in range(1,count+1):
        messages.append([r.hget(i, "Text"),
                        r.hget(i, "Time"),
                        r.hget(i, "User"),
                        i])
    messages = sorted(messages, key= lambda x: x[3])[::-1]
    return messages
@app.route("/", methods=["POST"])
def put_text():
    count_id = int(r.get("msg:id").decode())
    user, text = _check_user(f.request.form["content"])
    text_sub = {
                'Text': text,
                'Time': time.ctime(),
                'Hash':hash(f.request.form["content"]),
                'User': user
    }
    r.hmset(count_id+1, text_sub)
    r.incr("msg:id")
    return f.redirect("/", code=302)
def _check_user(text):
    match = re.search("\{(?P<user>.*):(?P<ps>.*)\}", text)
    if match == None:
        return ("nobody", text)
    ps = hashlib.md5()
    ps.update(str(match.group("ps")).encode("utf-8"))
    app.logger.info(ps.hexdigest())
    app.logger.info(r.get("usr:"+match.group("user")))
    auth = (ps.hexdigest().encode('utf-8') == r.get("usr:"+match.group("user")))
    #app.logger.info(match.group('ps'))
    app.logger.info(auth)
    return (("nobody", text)
            if (match == None)
            else
            (
            match.group('user') if auth else "nobody", text[match.end()+1:])
        )

@app.route("/mkuser")
def prompt_create_user():
    return f.render_template("mkuser.html")
@app.route("/mkuser", methods=["POST"])
def create_user():
    user= f.request.form['user']
    app.logger.info(f.request.form['password'])
    ps = hashlib.md5()
    ps.update(str(f.request.form['password']).encode('utf-8'))
    app.logger.info(ps.hexdigest())
    if not r.exists("usr:"+user):
        r.set("usr:"+user, ps.hexdigest())
        return f.redirect("/", code=302)
    else:
        return f.redirect("/", code=302)

if __name__ == "__main__":
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True)
