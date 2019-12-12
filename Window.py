import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel
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

    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        # Window variables
        width = 1500
        height = 1000

        # Label 1 variables
        i1_w = 1 / 3 * width
        i1_h = 2 / 3 * height
        i1_x = 1 / 4 * width - i1_w / 2
        i1_y = 1 / 16 * height

        # Label 2 variables
        i2_w = 1 / 3 * width
        i2_h = 2 / 3 * height
        i2_x = 3 / 4 * width - i2_w / 2
        i2_y = 1 / 16 * height

        self.imgPath = None

        # Buttons
        # Idee: Button Klasse die einen Initialisator hat, der Name und Ort in einem macht
        self.button = QPushButton("Upload", self)
        self.button.move(i1_x, i1_y + i1_h + 50)
        self.button.clicked.connect(self.img_upload)

        self.button_2 = QPushButton("Save", self)
        self.button_2.move(i2_x, i2_y + i2_h + 50)
        self.button_2.clicked.connect(self.img_save)

        self.button_3 = QPushButton("Edit", self)
        self.button_3.move(width / 2 - 3 / 4 * self.button_3.width(), i1_y + i1_h / 2)
        self.button_3.clicked.connect(self.img_treat)

        # Labels
        self.imageLabel = QLabel("Image", self)
        self.imageLabel.setAlignment(Qt.AlignTop)
        self.imageLabel.setStyleSheet("background-color: white; border: 1px inset grey")
        self.imageLabel.setGeometry(i1_x, i1_y, i1_w, i1_h)

        self.imageLabel_2 = QLabel("treated Image", self)
        self.imageLabel_2.setAlignment(Qt.AlignTop)
        self.imageLabel_2.setStyleSheet("background-color: white; border: 1px inset grey")
        self.imageLabel_2.setGeometry(i2_x, i2_y, i2_w, i2_h)

        # Window
        self.setGeometry(100, 100, width, height)
        self.setWindowTitle("Mammography Interpreter")
        self.show()

    # img_upload opens an image path via dialog and displays it scaled in our label
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

    # treatImage if self.imgPath of type image -> treat, else pass
    # TO DO: Warum funkt der if case nicht?
    def img_treat(self):
        if self.imgPath.endswith(('.jpg', '.jpeg', '.png')):

            apply_filter(self.imgPath) # Luccas Funktion

            pixmap = QPixmap('mama1.jpg').scaled(self.imageLabel_2.size(), Qt.KeepAspectRatio)
            self.imageLabel_2.setPixmap(pixmap)
        else:
            pass

    # save the image in Label 2 in a chosen directory
    # TO DO: if case einbauen, um keinen Err zu bekommen
    def img_save(self):
        fd = QFileDialog()
        fname = fd.getSaveFileName(self, 'Save File', 'C:\\Users\\Franziska\\Desktop', "(*.jpg *.jpeg *.png)")[0]
        print(fname)
        self.imageLabel_2.pixmap().save(fname) # don't save the resized file, take the other in storage


app = QApplication(sys.argv)
w = Window()
# TO DO: Add deletion of mama1.jpg (data safety)
sys.exit(app.exec_())



# function initialising
