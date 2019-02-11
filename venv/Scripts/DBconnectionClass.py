import sys
from PyQt5 import QtSql

class DB:

    def __init__(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QODBC")

    def CreateConnection(self):
        # Connect to the database ######################################################################################
        # self.db = QtSql.QSqlDatabase.addDatabase("QODBC")
        # db = QtSql.QSqlDatabase.addDatabase("QODBC3") Uses ODBC 3 drivers
        # db = QtSql.QSqlDatabase.addDatabase("QODBC", "myDB") Names this connection (if not provided, default)
        self.db.setDatabaseName("Driver={SQL Server};Server=jose-laptop;Database=garden;Trusted_Connection=yes")
        ok = self.db.open()
        if ok:
            return True
        else:
            return False

    def CloseConnection(self):
        self.db.close()


