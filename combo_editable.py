import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # add a title
        self.setWindowTitle('Combo box test')

        # set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # create a label
        my_label = qtw.QLabel("Pick something from list:")
        self.layout().addWidget(my_label)

        # create an combo box
        my_combo = qtw.QComboBox(self,
                                 editable=True,
                                 # insertPolicy=qtw.QComboBox.InsertAtTop,
                                 insertPolicy=qtw.QComboBox.InsertAtBottom,)
        # add item to cb
        my_combo.addItem("India", "IND")
        my_combo.addItem("United State of America","USA")

        self.layout().addWidget(my_combo)


        # create a button
        my_button = qtw.QPushButton("Click Me!", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        # show the app
        self.show()

        def press_it():
            # add name to label
            my_label.setText(f"You picked {my_combo.currentText()} with value of {my_combo.currentData()} with index of {my_combo.currentIndex()}!")


app = qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec_()

