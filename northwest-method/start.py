from form import *
from nw import *
import random
import numpy as np


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        self.ui.pushButton.clicked.connect(self.ok)
        self.ui.pushButton_2.clicked.connect(self.randomize)
        self.ui.pushButton_3.clicked.connect(self.randomize_2)
        self.ui.pushButton_4.clicked.connect(self.refresh)
        self.ui.pushButton_5.clicked.connect(self.solution)
        self.ui.pushButton_6.clicked.connect(self.show_prices)
        self.ui.pushButton_7.clicked.connect(self.show_plan)
        self.ui.pushButton_8.clicked.connect(self.next)

        self.ui.tableWidget.hide()
        self.ui.tableWidget_2.hide()
        self.ui.tableWidget_3.hide()
        self.ui.tableWidget_4.hide()

        self.ui.label_3.hide()
        self.ui.label_4.hide()
        self.ui.label_5.hide()

        self.ui.pushButton_2.hide()
        self.ui.pushButton_3.hide()
        self.ui.pushButton_4.hide()
        self.ui.pushButton_5.hide()
        self.ui.pushButton_6.hide()
        self.ui.pushButton_7.hide()
        self.ui.pushButton_8.hide()

        self.cel_func = 0
        self.plan = []

    def sizes(self):
        index_post = int(self.ui.comboBox.currentIndex())
        size_post = int(self.ui.comboBox.itemText(index_post))
        index_pot = int(self.ui.comboBox_2.currentIndex())
        size_pot = int(self.ui.comboBox_2.itemText(index_pot))
        return [size_post, size_pot]

    def set_col_row(self, a, b):
        self.ui.tableWidget.setColumnCount(a)
        self.ui.tableWidget.setRowCount(b)
        self.ui.tableWidget_2.setColumnCount(a)
        self.ui.tableWidget_3.setRowCount(b)
        self.ui.tableWidget_4.setColumnCount(a)
        self.ui.tableWidget_4.setRowCount(b)

    def ok(self):
        self.ui.pushButton_2.show()
        self.ui.pushButton_3.show()
        self.ui.pushButton_8.show()
        self.ui.tableWidget.show()
        self.ui.tableWidget_2.show()
        self.ui.tableWidget_3.show()
        self.ui.tableWidget.clear()
        self.ui.tableWidget_2.clear()
        self.ui.tableWidget_3.clear()
        self.ui.tableWidget_4.clear()

        self.ui.tableWidget_4.hide()
        self.ui.label_3.hide()
        self.ui.label_4.hide()
        self.ui.label_5.hide()
        self.ui.pushButton_4.hide()
        self.ui.pushButton_5.hide()
        self.ui.pushButton_6.hide()
        self.ui.pushButton_7.hide()

        size_post, size_pot = self.sizes()[0], self.sizes()[1]
        self.set_col_row(size_pot, size_post)

        item = QtWidgets.QTableWidgetItem()
        item.setText("Спрос")
        self.ui.tableWidget_2.setVerticalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("Мощность")
        self.ui.tableWidget_3.setHorizontalHeaderItem(0, item)

    def randomize(self):
        size_post, size_pot = self.sizes()[0], self.sizes()[1]
        for i in range(size_post):
            for j in range(size_pot):
                item = QtWidgets.QTableWidgetItem()
                item.setText("{}".format(random.randint(1, 8)))
                self.ui.tableWidget.setItem(i, j, item)

    def randomize_2(self):
        size_post, size_pot = self.sizes()[0], self.sizes()[1]
        for i in range(size_post):
            item = QtWidgets.QTableWidgetItem()
            item.setText("{}".format(random.randint(10, 70)))
            self.ui.tableWidget_3.setItem(i, 0, item)
        for j in range(size_pot):
            item = QtWidgets.QTableWidgetItem()
            item.setText("{}".format(random.randint(10, 70)))
            self.ui.tableWidget_2.setItem(0, j, item)

    def next(self):
        post, pot = [], []
        size_post, size_pot = self.sizes()[0], self.sizes()[1]
        for i in range(size_post):
            p = int(self.ui.tableWidget_3.item(i, 0).text())
            post.append(p)
        for j in range(size_pot):
            m = int(self.ui.tableWidget_2.item(0, j).text())
            pot.append(m)
        self.ui.label_4.setText("Суммарная мощность: {}".format(sum(post)))
        self.ui.label_5.setText("Суммарный спрос: {}".format(sum(pot)))
        self.ui.label_4.show()
        self.ui.label_5.show()
        if sum(post) == sum(pot):
            self.ui.pushButton_5.show()
            self.refresh()
        else:
            self.ui.pushButton_4.show()

    def refresh(self):
        self.ui.pushButton_5.show()
        self.ui.tableWidget.show()
        post, pot, costs = [], [], []
        size_post, size_pot = self.sizes()[0], self.sizes()[1]

        for i in range(size_post):
            p = int(self.ui.tableWidget_3.item(i, 0).text())
            post.append(p)
        for j in range(size_pot):
            m = int(self.ui.tableWidget_2.item(0, j).text())
            pot.append(m)
        for i in range(size_post):
            for j in range(size_pot):
                c = int(self.ui.tableWidget.item(i, j).text())
                costs.append(c)

        np_costs = np.array(costs)
        np_costs.shape = (size_post, size_pot)
        costs_list = [i for i in np_costs.tolist()]
        difference = int(abs(sum(post) - sum(pot)))

        if sum(post) < sum(pot):
            post.append(difference)
            costs_list.append([0 for i in range(len(pot))])
            self.ui.label_4.setText("Суммарная мощность: {}".format(sum(post)))
        if sum(pot) < sum(post):
            pot.append(difference)
            for i in range(len(post)):
                costs_list[i].append(0)
            self.ui.label_5.setText("Суммарный спрос: {}".format(sum(pot)))
        if sum(pot) == sum(post):
            costs_list = costs_list

        self.set_col_row(len(pot), len(post))

        for i in post:
            item = QtWidgets.QTableWidgetItem()
            item.setText("{}".format(i))
            self.ui.tableWidget_3.setItem(post.index(i), 0, item)
        for j in pot:
            item = QtWidgets.QTableWidgetItem()
            item.setText("{}".format(j))
            self.ui.tableWidget_2.setItem(0, pot.index(j), item)
        for i in range(len(post)):
            for j in range(len(pot)):
                item = QtWidgets.QTableWidgetItem()
                item.setText("{}".format(costs_list[i][j]))
                self.ui.tableWidget.setItem(i, j, item)

        norw = NorthWest(costs_list, pot, post)
        self.plan = norw.return_plan()
        self.cel_func = norw.return_c()

    def solution(self):
        self.ui.pushButton_6.show()
        self.ui.pushButton_7.show()
        self.ui.tableWidget_4.show()
        plan_list = self.plan
        plan_row = len(plan_list)
        plan_col = len(plan_list[0])
        for i in range(plan_row):
            for j in range(plan_col):
                item = QtWidgets.QTableWidgetItem()
                item.setText("{}".format(plan_list[i][j]))
                self.ui.tableWidget_4.setItem(i, j, item)
        self.ui.label_3.setText("Суммарные затраты: {}".format(self.cel_func))
        self.ui.label_3.show()

    def show_plan(self):
        self.ui.tableWidget_4.show()
        self.ui.tableWidget.hide()

    def show_prices(self):
        self.ui.tableWidget.show()
        self.ui.tableWidget_4.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    my_app = MyWin()
    my_app.show()
    sys.exit(app.exec_())
