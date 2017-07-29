import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def retrieve_lesson(js_file):
    data=json.load(js_file)
    for item in data:
        teachid=data["tid"]import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def retrieve_lesson(js_file):
    data=json.load(js_file)
    for item in data:
        teachid=data["tid"]
        cur = conn.cursor()
        cur.execute("SELECT * FROM lesson_plan WHERE teacher_id=", (teachid,))
        rows = cur.fetchall()
        jsonStr = json.dumps([row.toJSON() for row in rows])
    return jsonStr

def retrieve_pics(js_file):
    data=json.load(js_file)
    for item in data:
        teachid=data["tid"]
        cur = conn.cursor()
        cur.execute("SELECT picpath FROM pics WHERE teacher_id=", (teachid,))
        rows = cur.fetchall()
        jsonStr = json.dumps([row.toJSON() for row in rows])
    return jsonStr      

def retrieve_videos(js_file):
    data=json.load(js_file)
    for item in data:
        vid_id=data["vid"]
        teachid=data["tid"]
        less_id=data["lesid"]
        cur = conn.cursor()
        cur.execute("SELECT vidpath FROM videos WHERE videoid="+vid_id+" AND teacher_id="+teachid+" AND lesid="+less_id)
        rows = cur.fetchall()
        jsonStr = json.dumps([row.toJSON() for row in rows])
    return jsonStr

 
def main():
    database = "xxxx\pythonsqlite.db"
 
    conn = create_connection(database)
    with conn:
        
 
 
    if __name__ == '__main__':
    main()
        cur = conn.cursor()
        cur.execute("SELECT * FROM lesson_plan WHERE id=", (teachid,))
        rows = cur.fetchall()
        for row in rows:
        	print(row)

def retrieve_pics(js_file):
    data=json.load(js_file)
    for item in data:
        teachid=data["tid"]
        cur = conn.cursor()
        cur.execute("SELECT * FROM pics WHERE id=", (teachid,))
        rows = cur.fetchall()
        for row in rows:
        	print(row)


def main():
    database = "xxxx\pythonsqlite.db"
 
    conn = create_connection(database)
    with conn:
        
 
 
    if __name__ == '__main__':
    main()
