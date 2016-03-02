import flask as f
import redis
import time
'''
Todo:
- How do we post into db?


'''

app = f.Flask(__name__)
r = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route("/putMsg", methods=['POST'])
def put_messages():
    if (type(r.get("msg:id"))==None):
        r.set("msg:id", 0)
    count_id = int(r.get("msg:id").decode())
    user = "Nobody"
    text_sub = {
                'Text': f.request.form["content"],
                'Time': time.ctime(),
                'Hash':hash(f.request.form["content"]),
                'User': user
    }
    r.hmset(count_id+1, text_sub)
    r.incr("msg:id")
    return "Status OK"

@app.route("/getMsg", methods=['GET'])
def get_messages():
    return (_get_msg_by_id(f.request.args.get('id'))) if f.request.args.get('id') else "None"
def _get_msg_by_id(id):
    store = r.hgetall(id)
    return f.jsonify(
            text = store[b'Text'].decode('utf-8'),
            user = store[b'User'].decode('utf-8'),
            time = store[b'Time'].decode('utf-8')
            )

@app.route("/getMsg/all")
def get_messages_all():
    store = [r.hgetall(id) for id in range(1,int(r.get("msg:id")))]
    return str(store)



if __name__ == "__main__":
    app.run(debug=True)
