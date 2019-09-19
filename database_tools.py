import MySQLdb

db = object()
cursor = object()

def create_cursor():
    global db
    global cursor

    cursor = db.cursor()
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')

def connect_to_database(password):
    global db

    db = MySQLdb.connect(host="127.0.0.1",
                    user="root",
                    passwd=password,
                    db="parser")
    
    db.set_character_set('utf8')
    db.autocommit(True)

    create_cursor()
    



def insert_post(content_arr):
    global cursor

    print(content_arr)
    sql = "INSERT INTO parser.minecraft_modes(title, description, link) VALUES(%s, %s, %s)"
    values = (content_arr[0], content_arr[1], content_arr[2])

    cursor.execute(sql, values)



