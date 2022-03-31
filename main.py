import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # add a title
        self.setWindowTitle('Hello World!')

        # set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # create a label
        my_label = qtw.QLabel("Hello world from PyQt5!")
        self.layout().addWidget(my_label)
        self.show()

app = qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec_()

