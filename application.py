import flask
import psycopg2
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/items/all_items', methods=['GET'])
def get_items():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="d2platform_db",
        user="d2platform_adm",
        password="d2platform_adm")

    cur = conn.cursor()
    cur.execute("""SELECT * FROM d2platform.items""")

    res = cur.fetchall()
    print(res)
    conn.close()

    return jsonify(res)


app.run()
