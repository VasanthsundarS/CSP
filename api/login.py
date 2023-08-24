import cgi
import pymysql
print("Welcome To Code World")

form = cgi.FieldStorage()

mail = form.getvalue("email")
psd = form.getvalue("password")



# MySQL database configuration
conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="vsproj")
cursor = conn.cursor()

# Construct SQL query
sql = "SELECT * FROM userlogin where Mail_Id==%s"
values = (mail)

res = cursor.execute(sql, values)
print(res)
# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

