import sys
import DBconnectionClass
from PyQt5 import QtSql

# Open the database #############################################################################################
myDB = DBconnectionClass.DB()
print(myDB)
myDB.CreateConnection()

# Create and execute a query ####################################################################################
query = QtSql.QSqlQuery()
ok = query.exec_("select * from dbo.Farms")
# ok = query.exec_("select name, object_id, type_desc from sys.tables")
print(ok)

# Navigate the result set one record at a time ##################################################################
while (query.next()):
    print(int(query.value(0)),
          str(query.value(1)),
          str(query.value(2)),
          query.at())   # Row number

# Close the database ############################################################################################
myDB.CloseConnection()
