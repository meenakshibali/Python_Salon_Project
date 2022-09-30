from flask import Flask, render_template, request, redirect, url_for
import pymysql

app= Flask(__name__)

con= None
cur= None

def connectToDB():
    global con, cur
    con = pymysql.connect(host='localhost',user="root",password="",database="elegance")
    cur = con.cursor()
    
def disconnectDB():
    cur.close()
    con.close()

def getAllServiceData():
    connectToDB()
    selectquery="SELECT *FROM services;"
    cur.execute(selectquery)
    data= cur.fetchall()
    disconnectDB()
    return data

def insertToServiceTable(service_name,service_type,service_time, price):
    try:
        connectToDB()
        insertquery= "INSERT INTO services(service_name,service_type,service_time,price) VALUES(%s, %s, %s, %s);"
        cur.execute(insertquery, (service_name,service_type,service_time, price,))
        con.commit()
        disconnectDB()
        return True
    except:
        disconnectDB()
        return False


def deleteServiceTable(id):
    try:
        connectToDB()
        deletequery= "DELETE FROM  services WHERE id=%s;"
        cur.execute(deletequery, (id))
        con.commit()
        disconnectDB()
        return True
    except:
        disconnectDB()
        return False

@app.route("/")
@app.route("/index/")
def index():
    data = getAllServiceData()
    return render_template('index.html',data=data)

@app.route("/add/", methods=['GET','POST'])
def addService():
    if request.method== "POST":
        data= request.form
        if insertToServiceTable(data["txtService_Name"], data["txtService_Type"], data["txtService_Time"], data["txtPrice"]):
            message= "Record inserted Successfully"
        else:
            message= "Due to some issue couldnt insert record"
        return render_template("insert.html", message= message)
    return render_template("insert.html")


@app.route("/delete/")
def deleteService():
    id= request.args.get('id',type=int, default=1)
    deleteServiceTable(id)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug= True)