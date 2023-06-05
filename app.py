from flask import Flask 
import pyodbc

app = Flask(__name__)

driver = '{ODBC Driver 18 for SQL Server}'
database = 'adb'
server = 'tcp:assignment002.database.windows.net,1433'
username = "axg6991"
password = "27Animesh$"
conn= pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor() #cursor 
cursor.execute('''Select * from test''')
check_username=cursor.fetchall()
print(check_username)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"