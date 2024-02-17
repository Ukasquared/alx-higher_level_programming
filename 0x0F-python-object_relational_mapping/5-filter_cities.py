#!/usr/bin/python3

""" import the sqldb module and sys module """

if __name__ == "__main__":

  import MySQLdb
  import sys

  usaname = sys.argv[1]
  password = sys.argv[2]
  database = sys.argv[3]
  state_name = sys.argv[4]
  
  """ connect database """
  connection = MySQLdb.connect(host="localhost", port=3306, user=usaname, passwd=password, db=database)
  cur = connection.cursor()

  """ query the database """
  query = """ SELECT cities.name FROM cities
           INNER JOIN states ON states.id = cities.state_id
	   WHERE states.name = %s ORDER BY cities.id ASC """
  cur.execute(query, (state_name,))
  """ result returned by cur"""
  results = cur.fetchall()
  tuples = ()
  for result in results:
    tuples += result
  print(*tuples, sep=", ")
  cur.close()
  connection.close()
