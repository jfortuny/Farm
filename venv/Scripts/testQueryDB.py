import sys
import DBconnection
from PyQt5 import QtSql

# Open the database #############################################################################################
if not DBconnection.CreateConnection():
    exit(1)

# Create and execute a query ####################################################################################
query = QtSql.QSqlQuery()
ok = query.exec_("select name, object_id, type_desc from sys.tables")
print(ok)

# Navigate the result set one record at a time ##################################################################
while (query.next()):
    print(str(query.value(0)),
          int(query.value(1)),
          str(query.value(2)),
          query.at())   # Row number

# Close the database ############################################################################################
DBconnection.CloseConnection()
