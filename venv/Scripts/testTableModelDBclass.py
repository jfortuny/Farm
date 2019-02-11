import sys
import  DBconnectionClass
from PyQt5 import QtSql, QtCore
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

def initializeModel(model):
    model.setTable("dbo.Farms")
    model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    model.select()
    model.setHeaderData(0, Qt.Horizontal, "Id")
    model.setHeaderData(1, Qt.Horizontal, "Farm Name")
    model.setHeaderData(2, Qt.Horizontal, "Access")

def createView(title, model):
    view = QTableView()
    view.setGeometry((QtCore.QRect(100,100,500,200)))
    view.setModel(model)
    view.setWindowTitle(title)
    view.setColumnHidden(0, True)
    view.resizeColumnsToContents()
    return view

if __name__ == "__main__":

    # Initialize the application ####################################################################################
    app = QApplication(sys.argv)

    # Open the database #############################################################################################
    myDB = DBconnectionClass.DB()
    if not myDB.CreateConnection():
        sys.exit(-1)

    # Create the model ##############################################################################################
    modelFarms = QtSql.QSqlTableModel()
    initializeModel(modelFarms)

    # Create the view ###############################################################################################
    view1 = createView("Table Model, view 1", modelFarms)
    view2 = createView("Table Model, view 2", modelFarms)

    # Display the views #############################################################################################
    view1.show()
    view2.move(view1.x() + view1.width() + 20, view1.y())
    view2.show()

    sys.exit(app.exec_())

