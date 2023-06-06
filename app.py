from flask import Flask 
import pyodbc

app = Flask(__name__)

driver = '{ODBC Driver 18 for SQL Server}'
database = 'adb'
server = 'tcp:adbtestdata.database.windows.net,1433'
username = "kxs5434"
password = "root@123"
conn= pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor() #cursor 
cursor.execute('''Select * from dbo.all_day''')
query_output=cursor.fetchall()
print(query_output)

@app.route("/")
def hello_world():
    # sql = "SELECT * from users"
    # c1.execute(sql)
    # names = c1.fetchall()
    # except Exception as e:
    # print(e)
    # return query_output
    return "<p>Hello, World!</p>"