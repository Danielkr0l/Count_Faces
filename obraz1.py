from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2

class Obraz:
    def __init__(self, obrazek):
        self.obraz = cv2.imread(obrazek)
        self.liczba_ludzi = 0

    def policz_twarze(self):
        szare = cv2.cvtColor(self.obraz, cv2.COLOR_BGR2GRAY)
        rozpoznawanie = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        twarze = rozpoznawanie.detectMultiScale(
            szare,
            scaleFactor=1.11,
            minNeighbors=8,
            minSize=(15, 15)
        )
        self.osoby = []

        for (x, y, z, t) in twarze:
            self.osoby.append([x, y, z, t])

        return len(self.osoby)

    def bluruj(self):
        cv2.waitKey(0)
        for i in range(len(self.osoby)):
            roi = self.obraz[self.osoby[i][1]:self.osoby[i][1] + self.osoby[i][3],
                  self.osoby[i][0]:self.osoby[i][0] + self.osoby[i][2]]
            roi = cv2.GaussianBlur(roi, (23, 23), 30)
            self.obraz[self.osoby[i][1]:self.osoby[i][1] + roi.shape[0],
            self.osoby[i][0]:self.osoby[i][0] + roi.shape[1]] = roi
        return self.convert()

    def zaznacz(self):
        for i in range(len(self.osoby)):
            cv2.rectangle(self.obraz, (self.osoby[i][0], self.osoby[i][1]), (self.osoby[i][0] + self.osoby[i][2],
                                                                             self.osoby[i][1] + self.osoby[i][3]),(0, 255, 0), 2)
        return self.convert()

    def convert(self):
        img = self.obraz
        w, h, ch = img.shape
        if img.ndim == 1:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        qimg = QImage(img.data, h, w, 3 * h, QImage.Format_BGR888)
        qpixmap = QPixmap(qimg)

        return qpixmap

    def zapisz(self, name):
        name1 = 'zdjecia/'
        namesum = name1+name+'.jpg'
        cv2.imwrite(namesum, self.obraz)