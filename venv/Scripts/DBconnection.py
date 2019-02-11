import sys
from PyQt5 import QtSql

    
def CreateConnection():
    # Connect to the database ######################################################################################
    db = QtSql.QSqlDatabase.addDatabase("QODBC")
    # db = QtSql.QSqlDatabase.addDatabase("QODBC3") Uses ODBC 3 drivers
    # db = QtSql.QSqlDatabase.addDatabase("QODBC", "myDB") Names this connection (if not provided, default)
    db.setDatabaseName("Driver={SQL Server};Server=jose-laptop;Database=garden;Trusted_Connection=yes")
    ok = db.open()
    if ok:
        return True
    else:
        return False

def CloseConnection():
    db.close()
    

