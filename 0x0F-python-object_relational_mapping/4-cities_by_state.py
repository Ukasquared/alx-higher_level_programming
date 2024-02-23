#!/usr/bin/python3

""" import the sqldb module and sys module """

if __name__ == "__main__":

    import MySQLdb
    import sys

    usaname = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    """ connect database """
    connection = MySQLdb.connect(host="localhost", port=3306, user=usaname,
                                      passwd=password, db=database)
    cur = connection.cursor()

    """ query the database """
    query = """ SELECT cities.id, cities.name, states.name FROM cities\
           INNER JOIN states ON states.id = cities.state_id """
    cur.execute(query)
    """ loop throught the result returned by cur"""
    for result in cur:
        print(result)

    cur.close()
    connection.close()
