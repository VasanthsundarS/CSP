
import cgi
import pymysql
print("Welcome To Code World SignUp")

form=cgi.FieldStorage()

name=form.getvalue("name")
mail=form.getvalue("email")
psd=form.getvalue("password")

# name = "vs"
# mail = "vs23@gmail.com"
# psd = "vs23"

# import pymysql

# MySQL database configuration
conn = pymysql.connect(host="localhost", user="root", passwd="", db="vsproj")
cursor = conn.cursor()

# Construct SQL query
sql = "INSERT INTO userlogin (UserName, Password, Mail_Id) VALUES (%s, %s, %s)"
values = (name, psd, mail)

res = cursor.execute(sql, values)
print(res)
# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

