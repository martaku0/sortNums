import sys
from functools import partial

from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget, QHBoxLayout,
    QLineEdit, QMenu
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widget")

        self.setMinimumSize(QSize(300,300))

        layout = QVBoxLayout()


        title = QLabel("Wpisz ciąg liczb odzielonych przecinkiem:")
        layout.addWidget(title)
        global editText
        editText = QLineEdit()
        layout.addWidget(editText)
        global result
        result = QLabel("0")
        layout.addWidget(result)

        button1 = QPushButton("średnia")
        button1.clicked.connect(partial(self.clicked, "avg"))
        layout.addWidget(button1)
        button2 = QPushButton("minimum")
        button2.clicked.connect(partial(self.clicked, "min"))
        layout.addWidget(button2)
        button3 = QPushButton("maksimum")
        button3.clicked.connect(partial(self.clicked, "max"))
        layout.addWidget(button3)
        button4 = QPushButton("sortuj rosnąco")
        button4.clicked.connect(partial(self.clicked, "sortUp"))
        layout.addWidget(button4)
        button5 = QPushButton("sortuj malejąco")
        button5.clicked.connect(partial(self.clicked, "sortDown"))
        layout.addWidget(button5)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def contextMenuEvent(self, event):
        menu = QMenu(self)

        avg_action = QAction("średnia", self)
        avg_action.triggered.connect(partial(self.clicked, "avg"))
        menu.addAction(avg_action)

        min_action = QAction("minimum", self)
        min_action.triggered.connect(partial(self.clicked, "min"))
        menu.addAction(min_action)

        max_action = QAction("maksimum", self)
        max_action.triggered.connect(partial(self.clicked, "max"))
        menu.addAction(max_action)

        sort_up_action = QAction("sortuj rosnąco", self)
        sort_up_action.triggered.connect(partial(self.clicked, "sortUp"))
        menu.addAction(sort_up_action)

        sort_down_action = QAction("sortuj malejąco", self)
        sort_down_action.triggered.connect(partial(self.clicked, "sortDown"))
        menu.addAction(sort_down_action)

        menu.exec(self.mapToGlobal(event.pos()))

    def clicked(self, description):
        text = editText.text()

        if text:

            for c in text:
                if c.isnumeric() or c == ',':
                    continue
                else:
                    result.setText("Wrong input!")
                    return

            nums = text.split(',')

            while ("" in nums):
                nums.remove("")

            res = 0
            match description:
                case 'avg':
                    print('average')
                    res = self.countAvg(nums)
                case 'min':
                    print('minimum')
                    res = self.sorting(nums)[0]
                case 'max':
                    print('maksimum')
                    res = self.sorting(nums)[len(self.sorting(nums))-1]
                case 'sortUp':
                    print('sortowanie rosnące')
                    res = self.sorting(nums)
                case 'sortDown':
                    print('sortowanie malejące')
                    res = self.sorting(nums)
                    res.reverse()
                case _:
                    result.setText("Something went wrong")
                    return

            result.setText(str(res))

    def countAvg(self, nums):
        sum = 0
        count = 0
        for n in nums:
            if(n.isnumeric()):
                sum += int(n)
            count += 1
        return round(sum/count, 2)

    def sorting(self, nums):
        sorted_nums = []
        for n in nums:
            if sorted_nums == []:
                sorted_nums.append(n)
            else:
                found = False
                for i, s in enumerate(sorted_nums):
                    if int(n) < int(s):
                        sorted_nums.insert(i,n)
                        found = True
                        break
                if not found:
                    sorted_nums.append(n)



        return sorted_nums




app = QApplication()
window = MainWindow()
window.show()
app.exec()