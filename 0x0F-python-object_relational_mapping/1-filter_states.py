#!/usr/bin/python3

""" import modules """
if __name__ == '__main__':
  import sys
  import MySQLdb

  """ connect to existing database """
  connection = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
  """ create cursor to interact with database""" 
  cur = connection.cursor()
  """ execute an sql query to retrieve names of state frm states table"""
  cur.execute("SELECT s.id, s.name FROM states s WHERE s.name REGEXP '^[N]' ORDER BY s.id ASC")

  for row in cur:
    print(row)

  cur.close
  connection.close()
