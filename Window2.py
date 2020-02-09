import os
import sys
import cv2.cv2 as cv

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QGridLayout, QSizePolicy
from ProjetS9 import apply_filter


# TO DO: DocStrings

class Window(QWidget):
    """
    A class that builds a window of a GUI.

    Attributes
    ---------
    width : int
    height : int


    """
    # TO DO: ResizeEvent erstellen, damit Seitenverhältnisse erhalten bleiben
    # dafür evtl Layout verwerfen

    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        # Window variables
        width = 1500
        height = 1000

        self.imgPath = None

        # Buttons
        # Idee: Button Klasse die einen Initialisator hat, der Name und Ort in einem macht
        self.button = QPushButton("Upload", self)
        self.button.clicked.connect(self.img_upload)

        self.button_2 = QPushButton("Save", self)
        self.button_2.clicked.connect(self.img_save)

        self.button_3 = QPushButton("Edit", self)
        self.button_3.clicked.connect(self.img_treat)

        # Labels
        self.imageLabel = QLabel("Image", self)
        self.imageLabel.setAlignment(Qt.AlignTop)
        self.imageLabel.setStyleSheet("background-color: white; border: 1px inset grey")
        self.imageLabel.setScaledContents(1)

        self.imageLabel_2 = QLabel("treated Image", self)
        self.imageLabel_2.setAlignment(Qt.AlignTop)
        self.imageLabel_2.setStyleSheet("background-color: white; border: 1px inset grey")
        self.imageLabel_2.setScaledContents(1)

        # Layout
        grid = QGridLayout()

        grid.addWidget(self.imageLabel, 0, 0, 3, 2)
        grid.addWidget(self.button_3, 1, 2, 1, 1)
        grid.addWidget(self.imageLabel_2, 0, 3, 3, 2)
        grid.addWidget(self.button, 3, 0, 1, 2)
        grid.addWidget(self.button_2, 3, 3, 1, 2)

        self.setLayout(grid)

        self.setGeometry(100, 100, width, height) # setFixedSize öffnet mittig und fix
        self.setWindowTitle("TRIMED Mammography Interpreter")
        self.setWindowIcon(QIcon("LogoTriMed.jpeg"))
        self.show()

    # img_upload: opens an image path via dialog and displays it scaled in our label
    def img_upload(self):
        """
        Choose and show an image.

        :return: void
        """
        fd = QFileDialog()
        fname = fd.getOpenFileName(self, 'Open File', 'C:\\Users\\Franziska\\Desktop', "(*.jpg *.jpeg *.png)")[0]
        pixmap = QPixmap(fname).scaled(self.imageLabel.size(), Qt.KeepAspectRatio)
        self.imageLabel.setPixmap(pixmap)
        self.imgPath = fname

    # img_treat: if self.imgPath of type image -> treat and show in Label 2, else pass
    def img_treat(self):
        if self.imgPath is None:
            return
        if self.imgPath.endswith(('.jpg', '.jpeg', '.png')):

            apply_filter(self.imgPath) # Luccas Funktion

            pixmap = QPixmap('mama1.jpg').scaled(self.imageLabel_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.imageLabel_2.setPixmap(pixmap)
        else:
            return

    # img_save: if self.imgPath of type image -> save the image in Label 2 in a chosen directory, else pass
    def img_save(self):
        if self.imgPath is None:
            return
        fd = QFileDialog()
        fname = fd.getSaveFileName(self, 'Save File', 'C:\\Users\\Franziska\\Desktop', "(*.jpg *.jpeg *.png)")[0]
        print(fname)

        img = cv.imread('mama1.jpg')
        cv.imwrite(fname, img)

    # closeEvent: checks if path exits and remove it
    def closeEvent(self, event):
        if os.path.exists('mama1.jpg'):
            print("mama1.jpg exists")
            os.remove('mama1.jpg')
            print("mama1.jpg was removed")
        else:
            print("mama1.jpg doesn't exist")


app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())



# function initialising
