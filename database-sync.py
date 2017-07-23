import re
import mysql.connector

cnx = mysql.connector.connect(user='root', password='test', host='127.0.0.1', database='checkers')


cursor = cnx.cursor()

#cursor.execute("SHOW TABLES")
#tables = cursor.fetchall()
#print tables

#cursor.execute("DESCRIBE states_tbl")
#states_format = cursor.fetchall()
#print states_format

#cursor.execute("SELECT * FROM states_tbl")
#states_content = cursor.fetchall()
#print states_content
state = "frozenset([32, 33, 34, 35, 19, 24, 25, 26, 28, 29, 30, 31]):frozenset([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 17])"

try:
    cursor.execute('INSERT INTO states_tbl (state) VALUES ("frozenset([32, 33, 34, 35, 19, 24, 25, 26, 28, 29, 30, 31]):frozenset([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 17])");')
    cnx.commit()
except:
    cnx.rollback()
cmd1 = 'SELECT state_id from states_tbl where state = "' + state + '";'
#print cmd1
cursor.execute(cmd1)
state_id_str = str(cursor.fetchall())
state_id = re.findall(r'\d+',state_id_str)[0]
print state_id
action = "(13, 17)" 

action_cmd = 'INSERT INTO actions_tbl (action, state_id, p_result, n_result) VALUES ("' + action + '", ' + state_id + ', 0, 0)'
try:
    cursor.execute(action_cmd)
    cnx.commit()
except:
    cnx.rollback()
#reply = cursor.fetchall()
#print reply

#cmd_add_state = "INSERT INTO states_tbl ()"



cnx.close()
