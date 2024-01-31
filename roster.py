import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

file_name = input('Enter file name: ')
if len(file_name) < 1:
    file_name = 'roster_data_sample.json'

#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

open_file = open(file_name).read()
json_data = json.loads(open_file)

for entry in json_data:

    given_name = entry[0]
    title = entry[1]
    instructor = entry[2]

    print((given_name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( given_name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (given_name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, instructor) )

    conn.commit()

cur.execute("""SELECT hex(User.name || Course.title || Member.role) AS YYY FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY YYY""")
my_fetch = cur.fetchone()
print("RESULT: "+str(my_fetch))
cur.close()
conn.close()
