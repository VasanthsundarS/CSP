import pymysql

# database connection
def dbConn():
    connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="vsproj")
    cursor = connection.cursor()
    print(connection)
    return connection, cursor

def insDat():
    try:
        connection, cursor = dbConn()
        nam = 'vasu'
        txt = "Hi I'm Vasu This is Check Second"
        pic = None
        fil = None
        # nam = 'vSchkFile'
        # txt = "Hi I'm Vasu This is Check"
        # pic = convertToBinaryData('inDats/vs.JPG')
        # fil = convertToBinaryData('inDats/vsImport.py')
        iq = '''INSERT INTO vscode(IName, IFile, IText, IIMage) VALUES (%s, %s, %s, %s);'''
        idat = (nam, fil, txt, pic)
        res = cursor.execute(iq, idat)
        connection.commit()

    except Exception as err:
        print("Failed to Insert Data from MySQL table {}".format(err))

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("MySQL connection is closed")     

def getDat():
    try:
        connection, cursor = dbConn()
        phot = 'strDats/Dora.JPG'
        filooofil = 'strDats/Mt.txt'
        # Get All Data
        gqal = """select * from vscode"""
        cursor.execute(gqal)
        # Get Specific Id Date
        # gid = ""
        # gqid = """select * from vscode where id = %s"""
        # cursor.execute(gqal, (gid))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Text = ", row[3])
            pic = row[-1]
            fil = row[2]
            print("Storing employee image and bio-data on disk \n")
            if pic:
                write_file(pic, phot)
            if fil:
                write_file(fil, filooofil)

    except Exception as err:
        print("Failed to Get Data from MySQL table {}".format(err))

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def upDat():
    try:
        connection, cursor = dbConn()
        uid = 4
        gqid = """select * from vscode where id = %s"""
        cursor.execute(gqid, (uid))
        record = cursor.fetchone()
        nam = record[1]
        txt = record[3]
        pic = record[-1]
        fil = record[2]
        txt = "Hey, chkEdit By, VsDevGuru"
        # pic = convertToBinaryData('vs.JPG')
        # fil = convertToBinaryData('vsImport.py')
        uqry = """update vscode set IName=%s, IFile=%s, IText=%s, IImage=%s where Id=%s"""
        udat = (nam, fil, txt, pic, uid)
        res = cursor.execute(uqry, udat)
        connection.commit()
    except Exception as err:
        print("Failed to Update Data from MySQL table {}".format(err))

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def delDat():
    try:
        connection, cursor = dbConn()
        uid = 3
        dqry = """Delete from vscode where Id=%s"""
        ddat = (uid)
        cursor.execute(dqry, ddat)
        connection.commit()
    except Exception as err:
        print("Failed to Delete Data from MySQL table {}".format(err))

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
    
def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

# insDat()
# getDat()
# upDat()
# delDat()
