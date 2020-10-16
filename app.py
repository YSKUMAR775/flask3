from flask import Flask, jsonify, request
import pymysql


app = Flask(__name__)


@app.route("/aws2", methods=['Get'])
def sun2():
    mydb = pymysql.connect(host='database.c42ojr1a1cpj.ap-south-1.rds.amazonaws.com',
                           user='root',
                           password='yskumar775',
                           db='aws')

    cur = mydb.cursor()

    query = "select * from aws_table"

    cur.execute(query)

    s = cur.fetchall()

    li = []
    for i in s:

        dic = {'id': i[0], 'names_info': i[1], 'contact': i[2], 'mail': i[3]}
        li.append(dic)

    return jsonify(li)


@app.route("/aws/<int:id>", methods=['Post'])
def sun(id):
    data = request.get_json()

    a = data['names_info']
    b = data['contact']
    c = data['mail']
    d = id

    mydb = pymysql.connect(host='database.c42ojr1a1cpj.ap-south-1.rds.amazonaws.com',
                           user='root',
                           password='yskumar775',
                           db='aws')

    cur = mydb.cursor()

    query = "update aws_table set names_info = '"+str(a)+"', contact = '"+str(b)+"', mail = '"+str(c)+"' where id = '"+str(d)+"'"

    cur.execute(query)

    mydb.commit()

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
