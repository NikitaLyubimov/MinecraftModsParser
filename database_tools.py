import MySQLdb

db

def connect_to_database(password):
    global db

    db = MySQLdb.connect(host="127.0.0.1",
                    user="root",
                    passwd=password,
                    db="parser")
    
cursor = db.cursor()

def insert_post(content_arr):
    global cursor

    cursor.execute(f"INSERT INTO minecraft_modes(title, description, link) VALUES({content_arr[0]}, {content_arr[1]}, {content_arr[2]})")


