import os
import pymysql as mysql




## A static variable with the path to the DB credentials
path_to_credentials = os.path.expanduser("./replica.my.cnf")

    ## Connect to a WM database and returns the pymysql.connections.Connection object
    #  Connects using the replica.my.cnf file
    #  @param languagecode The Languagecode of that project in ISO-639-1
def connect_to_wikipedia(languagecode):
    try:
        mysql_con_read = mysql.connect(host=languagecode + "wiki.analytics.db.svc.eqiad.wmflabs",
                                       db=languagecode + 'wiki_p', read_default_file= path_to_credentials,
                                       charset='utf8mb4')  # utf8mb4
        return mysql_con_read
    except:
        print('This language has no database or we cannot connect to it: ' + languagecode)
        pass


