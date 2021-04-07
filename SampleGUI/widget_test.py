# widget_test.py
##
# Asis A Sotelo
# January 20, 2021
##
# A Template for Widget Tests
##


import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class IPv4Validator(qtg.QValidator):
    """Enforce entry of IPv4 Addresses"""


## The Main Window
class MainWindow(qtw.QWidget):
    def __init__(self):
        """MainWindow Constructor"""

        super().__init__()
        # MAIN UI CODE GOES HERE

        label = qtw.QLabel('Hello Widgets!', self)
        label.setText("Hi There, Widgets!")
        label.setFixedSize(150,40) ## Sets the pixel dimenstions of the label
        print(label.text())

        line_edit = qtw.QLineEdit(
            'default value',
            self,
            placeholderText='Type Here',
            clearButtonEnabled=True,
            maxLength=20)

        line_edit.setMinimumSize(150,15)
        line_edit.setMaximumSize(400,50)

        button = qtw.QPushButton(
            "Push Me",
            self,
            checkable=True,
            checked=True,
            shortcut=qtg.QKeySequence('Ctrl+p'))

        combobox = qtw.QComboBox(
            self,
            editable=True,
            insertPolicy=qtw.QComboBox.InsertAtTop

        )

        combobox.addItem('Lemon', 1)
        combobox.addItem('Peach', 'Ohh I like peaches')
        combobox.addItem('Strawberry', qtw.QWidget)
        combobox.insertItem(1, 'Radish', 2)

        datetimebox = qtw.QDateTimeEdit(
            self,
            date=qtc.QDate.currentDate(),
            time=qtc.QTime(12, 30),
            calendarPopup=True,
            maximumDate=qtc.QDate(2030, 1, 1),
            maximumTime=qtc.QTime(17, 0),
            displayFormat='yyyy-MM-dd HH:mm'
        )

        spinbox = qtw.QSpinBox(
            self,
            value=12,
            maximum=100,
            minimum=10,
            prefix='$',
            suffix=' + Tax',
            singleStep=5
        )

        spinbox.setSizePolicy(qtw.QSizePolicy.Fixed,qtw.QSizePolicy.Preferred)

        textedit = qtw.QTextEdit(
            self,
            acceptRichText=False,
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=25,
            placeholderText='Enter your text here'
        )
        textedit.setSizePolicy(
            qtw.QSizePolicy.MinimumExpanding,qtw.QSizePolicy.MinimumExpanding
        )

        ## QVBoxLayout

        layout = qtw.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(label)
        layout.addWidget(line_edit)

        sublayout = qtw.QHBoxLayout()
        layout.addLayout(sublayout)
        
        sublayout.addWidget(button)
        sublayout.addWidget(combobox)

        ## QGridLayout 

        grid_layout = qtw.QGridLayout()
        #layout.addLayout(grid_layout)
        grid_layout.addWidget(spinbox,0,0)
        grid_layout.addWidget(datetimebox,0,1)
        grid_layout.addWidget(textedit,1,0,2,2)

        ## QFormLayout

        form_layout = qtw.QFormLayout()
        layout.addLayout(form_layout)

        form_layout.addRow('Item 1', qtw.QLineEdit(self)) 
        form_layout.addRow('Item 2',qtw.QLineEdit(self))
        form_layout.addRow(qtw.QLabel('<b>This is a label-only row</b>'))

        ## QTabWidget

        tab_widget = qtw.QTabWidget(
            movable=True,
            tabPosition=qtw.QTabWidget.West,
            tabShape=qtw.QTabWidget.Triangular,
        )
        layout.addWidget(tab_widget)

        
        container = qtw.QWidget(self)
        container.setLayout(grid_layout)

        tab_widget.addTab(container,"Drop the Top")

        ## QGroubBox

        groupbox = qtw.QGroupBox(
            'Buttons',
            checkable=True,
            checked=True,
            alignment=qtc.Qt.AlignHCenter,
            flat=True)
        groupbox.setLayout(qtw.QHBoxLayout())
        groupbox.layout().addWidget(qtw.QPushButton('OK'))
        groupbox.layout().addWidget(qtw.QPushButton('Cancel'))
        layout.addWidget(groupbox)
        
        ## Validating Widgets







        # END MAIN UI CODE

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
