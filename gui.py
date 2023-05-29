import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import obraz1



class LiczaczLudzi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initui()
        self.label = QLabel(self)
        self.pixmap = False



    def initui(self):
        QWidget.__init__(self)
        self.setWindowTitle('Zliczacz Ludzi')
        self.setGeometry(100, 60, 1300, 800)

        bckgr_image = QImage("test.png")
        _image = bckgr_image.scaled(QSize(1300, 800))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(_image))
        self.setPalette(palette)

        self.buttonAddPhoto = QPushButton('DODAJ ZDJĘCIE', self)
        self.buttonBlur = QPushButton('Bluruj twarze', self)
        self.buttonTag = QPushButton('Oznacz twarze', self)
        self.nameoffile = QLineEdit('nowy_plik', self)
        self.nameoftype = QLineEdit('.jpg', self)
        self.buttonSave = QPushButton('Zapisz', self)
        self.buttonAddAnother = QPushButton('Nowe zdjęcie', self)
        self.counterLabel = QLabel(self)
        self.counterNumb = QLabel(self)

        self.buttonAddPhoto.setGeometry(300, 350, 400, 80)
        self.buttonAddPhoto.clicked.connect(self.on_open)
        self.buttonAddPhoto.setFont(QFont('Verdana', 23))

        self.buttonBlur.setGeometry(1050, 181, 213, 49)
        self.buttonBlur.clicked.connect(self.on_blur)
        self.buttonBlur.setFont(QFont('Verdana', 13))

        self.buttonTag.setGeometry(1050, 231, 213, 49)
        self.buttonTag.clicked.connect(self.on_tag)
        self.buttonTag.setFont(QFont('Verdana', 13))

        self.nameoffile.setGeometry(1051, 310, 173, 39)
        self.nameoffile.setFont(QFont('Verdana', 10))
        self.nameoffile.setAlignment(Qt.AlignCenter)
        self.nameoffile.setMaxLength(20)
        self.nameoffile.setFrame(True)

        self.nameoftype.setGeometry(1220, 310, 40, 39)
        self.nameoftype.setFont(QFont('Verdana', 8))
        self.nameoftype.setReadOnly(True)

        self.buttonSave.setGeometry(1050, 351, 213, 49)
        self.buttonSave.clicked.connect(self.on_save)
        self.buttonSave.setFont(QFont('Verdana', 13))

        self.buttonAddAnother.setGeometry(1050, 421, 213, 49)
        self.buttonAddAnother.clicked.connect(self.on_open)
        self.buttonAddAnother.setFont(QFont('Verdana', 13))


        self.counterLabel.setGeometry(1050, 501, 213, 49)
        self.counterLabel.setFont(QFont('Verdana', 11))
        self.counterLabel.setText('Liczba ludzi na zdjęciu : ')
        self.counterLabel.setAlignment(Qt.AlignCenter)

        self.counterNumb.setGeometry(1050, 551, 213, 49)
        self.counterNumb.setFont(QFont('Verdana', 15))
        self.counterNumb.setAlignment(Qt.AlignCenter)

        self.show()

    def on_open(self):
        options = QFileDialog.Options()
        file_name = QFileDialog.getOpenFileName(self, "Wybierz zdjęcie", "", "JPG Files (*.jpg);;PNG Files (*.png) ;; BMP Files (*.bmp)",
                                                         options=options)
        self.img = obraz1.Obraz(file_name[0])
        self.pixmap = QPixmap(file_name[0])
        self.pixi = self.pixmap.scaled(900, 500, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixi)
        string_counter = str(self.img.policz_twarze())
        self.counterNumb.setText(string_counter)
        self.label.setGeometry(50, 50, 900, 700)
        self.label.setAlignment(Qt.AlignCenter)
        self.nameoffile.show()
        self.label.show()
        self.counterNumb.show()
        self.buttonAddPhoto.hide()
        self.buttonAddAnother.show()

    def on_blur(self):
        pix = self.pixmap
        if not pix:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('brak zdjęcia!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            self.pixmap = self.img.bluruj()
            self.pixi = self.pixmap.scaled(900, 500, Qt.KeepAspectRatio)
            self.label.setPixmap(self.pixi)
            self.label.setGeometry(50, 50, 900, 700)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.show()

    def on_tag(self):
        pix = self.pixmap
        if not pix:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('brak zdjęcia!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        self.pixmap = self.img.zaznacz()
        self.pixi = self.pixmap.scaled(900, 500, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixi)
        self.label.setGeometry(50, 50, 900, 700)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.show()

    def on_save(self):
        pix = self.pixmap
        if not pix:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('brak zdjęcia!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        self.img.zapisz(self.nameoffile.text())


app = QApplication(sys.argv)
window = LiczaczLudzi()
sys.exit(app.exec())
