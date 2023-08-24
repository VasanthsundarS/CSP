from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'vsproj'
 
mysql = MySQL(app)

print(mysql)

@app.route('/codeStore')
def form():
    return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM userlogin where Mail_Id=%s and Password=%s"
        cursor.execute(sql, (email, password))
        isUser = cursor.fetchall()
        if not isUser:
            return "Invalid Username and Password, Please provide Correctly"
        print("INFO", f"Login Id: {isUser[0][0]}")
        sql = f"SELECT * FROM vscode where LoginId={isUser[0][0]}"
        cursor.execute(sql)
        isData = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        return render_template('platform.html', data=isData)
    
@app.route('/signUp', methods = ['POST', 'GET'])
def signUp():
    try:
        if request.method == 'GET':
            return render_template('index.html')
        
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            cursor = mysql.connection.cursor()
            # Construct SQL query
            isExistSql = "SELECT * FROM userlogin where Mail_Id=%s"
            cursor.execute(isExistSql, (email,))
            isExistMail = cursor.fetchall()
            if isExistMail:
                print("INFO", "User Already EXist")
                return "User Already EXist"
            sql = "INSERT INTO userlogin (UserName, Password, Mail_Id) VALUES (%s, %s, %s)"
            values = (name, password, email)
            cursor.execute(sql, values)
            mysql.connection.commit()
            cursor.close()
            # print("INFO", "User Generated Successfully")
            return render_template('index.html')
        
    except Exception as err:
        print("ERROR", "Failed to Insert Data from MySQL table {}".format(err))

@app.route('/addDatas', methods = ['POST', 'GET'])
def addDatas():
    try:
        if request.method == 'GET':
            return "Login via the login Form"
        if request.method == 'POST':
            name = request.form['name']
            text = request.form['text']
            picture = request.form['picture']
            file = request.form['file']
            cursor = mysql.connection.cursor()
            iq = '''INSERT INTO vscode(LoginId, IName, IFile, IText, IIMage) VALUES (%s, %s, %s, %s, %s);'''
            res = cursor.execute(iq, (name, text, picture, file))
            mysql.connection.commit()

    except Exception as err:
        print("ERROR", "Failed to Added Data from MySQL table {}".format(err))

app.run(host='localhost', port=5000)