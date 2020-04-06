#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#       YUSUF ALİ KILIÇ
#
import math
from queue import PriorityQueue
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem

ARKAPLAN = "#30D5C8"
tahtaTamam = False


class Ui_MainWindow(QMainWindow):
    def setupUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 600)
        MainWindow.setFixedSize(818, 600)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 800, 420))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setMaximumWidth(800)
        self.tableWidget.setMaximumHeight(430)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 460, 692, 34))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.openFileNameDialog)
        self.horizontalLayout.addWidget(self.toolButton)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(5, 540, 821, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Load Input File"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Online"))
        self.pushButton.setToolTip(_translate("MainWindow","<html><head/><body><p style='color:red;'>This button is unavaliable!</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Offline(Using A*)"))
        self.pushButton_3.setText(_translate("MainWindow", "Offline(Using RBFS)"))
        self.pushButton_3.setToolTip(_translate("MainWindow","<html><head/><body><p style='color:red;'>This button is unavaliable!</p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Offline(Using SMA*)"))
        self.pushButton_4.setToolTip(_translate("MainWindow","<html><head/><body><p style='color:red;'>This button is unavaliable!</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "NOT: KIRMIZI BAŞLANGIÇ NOKTASI, SARI GİDİŞ YOLU VE YEŞİL HEDEFTİR. DİKDÖRTGENDE İNDEKS 0 DAN BAŞLAMAKTADIR"))

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

        if fileName:
            f = open(fileName, 'r')
            with f:
                lines = f.readlines()
                x: int = 1
                for line in lines:
                    if x == 1:
                        print("Tahta")
                        board = line.split(',')
                        print("x: " + str(board[0]) + " y: " + str(board[1]))
                    elif x == 2:
                        print("Robot")
                        robot = line.split(',')
                        print("x: " + str(robot[0]) + " y: " + str(robot[1]))
                    elif x == 3:
                        print("Goal State")
                        goal = line.split(',')
                        print("x: " + str(goal[0]) + " y: " + str(goal[1]))
                    elif x == 4:
                        obstacle_count = line
                        print("obstacle count: " + obstacle_count)
                    elif x == 5:
                        print("Obstacles Coordinates:")
                        obstacle = line.split('-')
                        for i in range(int(obstacle_count)):
                            print(obstacle[i])
                            i += 1
                        print(obstacle)
                    else:
                        print("HaTA!!")
                    x += 1
                board = board[0], board[1].replace('\n','')
                robot = robot[0], robot[1].replace('\n','')
                goal = goal[0], goal[1].replace('\n','')
                self.boarduAyarla(board,robot,goal,obstacle_count,obstacle)

    def boarduAyarla(self,boardBoyut,robotCoor,goalCoor,obstacleCount,obstacleCoors):
        print(boardBoyut)
        self.tableWidget.setColumnCount(int(boardBoyut[0]))
        self.tableWidget.setRowCount(int(boardBoyut[1]))
        mesafeX= 800 // int(boardBoyut[0])
        mesafeY = 430 // int(boardBoyut[1])
        print(mesafeX)
        print(mesafeY)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(mesafeX)
        self.tableWidget.verticalHeader().setDefaultSectionSize(mesafeY)

        for i in boardBoyut[0]:
            itemX = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(int(i), itemX)
            itemX.setText("New Row"+i)
        for j in boardBoyut[1]:
            itemY = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(int(j), itemY)
            itemY.setText("New Column"+j)
        self.robotuKoy(int(robotCoor[0]),int(robotCoor[1]))
        self.goaluBelirt(int(goalCoor[0]),int(goalCoor[1]))
        self.engelleriKoy(obstacleCount,obstacleCoors)
        tahtaTamam = True
        if tahtaTamam == True:
            self.pushButton_2.setEnabled(True)
            self.pushButton_2.clicked.connect(lambda :self.a_star(robotCoor, goalCoor, boardBoyut, obstacleCount, obstacleCoors))

    def robotuKoy(self,X,Y):
        print('*********************************************')
        print('Robot yeri ayarlamak için fonksiyona girdi')
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./robo_svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.tableWidget.setItem(X, Y, item)
        print('Robot yeri ayarlamak için fonksiyondan çıktı')
        print('*********************************************')

    def goaluBelirt(self,X,Y):
        print('*********************************************')
        print('Goal yeri ayarlamak için ve yeşile boyamak için fonksiyona girdi')
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.tableWidget.setItem(X, Y, item)
        print('Goal yeri ayarlamak için fonksiyondan çıktı')
        print('*********************************************')

    def engelleriKoy(self,obstacle_num,obstacles):
        print('*********************************************')
        print('Engellerin yeri ayarlamak için ve siyaha boyamak için fonksiyona girdi')
        for i in range(int(obstacle_num)):
            item = QtWidgets.QTableWidgetItem()
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            item.setBackground(brush)
            obstaclesCoordinates = obstacles[int(i)].split(',')
            obstaclesX = int(obstaclesCoordinates[0])
            obstaclesY = int(obstaclesCoordinates[1])
            item.setText(obstaclesCoordinates[0] + "," + obstaclesCoordinates[1])
            self.tableWidget.setItem(obstaclesX, obstaclesY, item)
        print('Engellerin yeri ayarlamak için fonksiyondan çıktı')
        print('*********************************************')

    def a_star(self,start,end,board,obstacle_count,obstacle):
        start_str = start
        start = int(start[0]),int(start[1])
        end_str = end
        end = int(end[0]), int(end[1])
        board = int(board[0]), int(board[1])
        obstacle_count = int(obstacle_count.replace('\n',''))
        pq = PriorityQueue()
        pq.put((0, start))
        came_from = {start: None}
        costs = {start: 0}
        while not pq.empty():
            current_pos = pq.get()[1]
            if current_pos == end:
                print(current_pos)
                break
            neighbors = self.get_neighbors(current_pos[0], current_pos[1],board,obstacle_count,obstacle)
            for neighbor in neighbors:
                new_cost = costs[current_pos] + 1

                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    priority = new_cost + self.heuristic_distance(neighbor, end)
                    pq.put((priority, neighbor))
                    came_from[neighbor] = current_pos

        #print(came_from)
        path = self.find_path(start, end, came_from)
        print(path)
        for i in path:
            if i!=start:
                if i!=end:
                    item = QtWidgets.QTableWidgetItem()
                    brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    item.setBackground(brush)
                    #print(i[0],i[1])
                    self.tableWidget.setItem(i[0], i[1], item)



    def heuristic_distance(self,pos, end_pos):
        dx = abs(pos[0] - int(end_pos[0]))
        dy = abs(pos[1] - int(end_pos[1]))
        return dx + dy

    def find_path(self,start, end, came_from):
        path = [end]
        current = end
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path


    def get_neighbors(self,current_posX, current_posY,board,obstacle_count,obstacle):
        neighborhood = []
        komsuSag = (int(current_posX)+1,int(current_posY))
        komsuSol = (int(current_posX)-1,int(current_posY))
        komsuUst = (int(current_posX),int(current_posY)+1)
        komsuAlt = (int(current_posX),int(current_posY)-1)
        if True == self.uygun_mu(komsuSag,board,obstacle_count,obstacle):
            neighborhood.append(komsuSag)
        if True == self.uygun_mu(komsuSol,board,obstacle_count,obstacle):
            neighborhood.append(komsuSol)
        if True == self.uygun_mu(komsuUst,board,obstacle_count,obstacle):
            neighborhood.append(komsuUst)
        if True == self.uygun_mu(komsuAlt,board,obstacle_count,obstacle):
            neighborhood.append(komsuAlt)

        return neighborhood


    def get_cost(self):
        pass

    def uygun_mu(self,current_positon,board,obstacle_count,obstacles):
        uygun = True
        if current_positon[0] >= 0 & current_positon[1] >=0:
            uygun = True
        if current_positon[0] <=int(board[0]) & current_positon[1] <= int(board[1]):
            uygun = True
        else:
            uygun = False

        for i in range(int(obstacle_count)):
            obstaclesCoordinates = obstacles[int(i)].split(',')
            obstaclesX = int(obstaclesCoordinates[0])
            obstaclesY = int(obstaclesCoordinates[1])
            if (obstaclesX==current_positon[0]) & (obstaclesY==current_positon[1]):
                uygun = False
                return uygun
            else:
                uygun = True
        return uygun


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    MainWindow.show()
    sys.exit(app.exec_())
