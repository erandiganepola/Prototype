# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProcessUi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import codecs
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import sqlite3
import math
from nltk.util import ngrams
from collections import Counter
import operator

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(657, 502)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 380, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(335, 380, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 420, 133, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 420, 133, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.textEdit_2 = QtGui.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(335, 30, 315, 341))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 415, 141, 31))
        self.label.setLineWidth(1)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(335, 415, 141, 31))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 460, 133, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(510, 460, 133, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 455, 141, 31))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(335, 455, 151, 31))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(130, 10, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(470, 10, 71, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 315, 341))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Process text", None))
        self.pushButton.setText(_translate("Form", "Process", None))
        self.pushButton_2.setText(_translate("Form", "Clear", None))
        self.label.setText(_translate("Form", "Jaccard similarity using Bigram", None))
        self.label_2.setText(_translate("Form", "Jaccard similarity using Trigram", None))
        self.label_3.setText(_translate("Form", "Cosine similarity using Bigram", None))
        self.label_4.setText(_translate("Form", "Cosine similarity using Trigram", None))
        self.label_5.setText(_translate("Form", "Document 1", None))
        self.label_6.setText(_translate("Form", "Document 2", None))
        self.pushButton.clicked.connect(self.buttonProcessClick)
        self.pushButton_2.clicked.connect(self.buttonClearClick)

    def buttonClearClick(self):
        self.textEdit.clear()
        self.textEdit_2.clear()

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()

    def buttonProcessClick(self):
        conn = sqlite3.connect('../Test/synDb.db')

        def build_vector(iterable1, iterable2):
            counter1 = Counter(iterable1)
            counter2 = Counter(iterable2)
            all_items = set(counter1.keys()).union(set(counter2.keys()))
            vector1 = [counter1[k] for k in all_items]
            vector2 = [counter2[k] for k in all_items]
            return vector1, vector2

        def dot_product2(v1, v2):
            return sum(map(operator.mul, v1, v2))

        def vector_cos5(v1, v2):
            prod = dot_product2(v1, v2)
            len1 = math.sqrt(dot_product2(v1, v1))
            len2 = math.sqrt(dot_product2(v2, v2))
            return prod / (len1 * len2)

        doc1 = self.textEdit.toPlainText()
        doc2 = self.textEdit_2.toPlainText()
        sinstopwords = set(stopwords.words("sinhala"))
        p = re.compile('[0-9]{1,9}')
        p1 = re.compile('[0-9]{1,9}.[0-9]{1,9}')
#removing hyphans
        data1 = doc1.replace('-','')
        data2 = doc2.replace('-','')
        data3 = data1.replace("'",'')
        data4 = data2.replace("'",'')
#replacing numbers with 0 and tokenization
        newdata1 = p1.sub('0', p.sub('0',data3))
        words1 = word_tokenize(newdata1)
        newdata2 = p1.sub('0', p.sub('0',data4))
        words2 = word_tokenize(newdata2)
#removing stop words and puntuations        
        filtered_sentence1 = [w1 for w1 in words1 if not w1 in sinstopwords]
        filtered_sentence2 = [w2 for w2 in words2 if not w2 in sinstopwords]
		
        outtext1 = ''
        outtext2 = ''
        for index3,i in enumerate(filtered_sentence1):
            q1 = "SELECT LEMMA FROM LEMMATB WHERE WORD='" + str(i) + "'"
            cursor = conn.execute(q1)
            for row in cursor:
                if (row[0] != None):
                    filtered_sentence1[index3] = row[0]

        for index4,j in enumerate(filtered_sentence2):
            q2 = "SELECT LEMMA FROM LEMMATB WHERE WORD='" + str(j) + "'"
            cursor1 = conn.execute(q2)
            for row in cursor1:
                if (row[0] != None):
                    filtered_sentence2[index4] = row[0]

        for index,i in enumerate(filtered_sentence1):
            q1 = "SELECT WORD1 FROM WORDTB WHERE WORD1='" + str(i) + "' OR WORD2='" + str(i) + "' OR WORD3='" + str(i) + "' OR WORD4='" + str(i) + "' OR WORD5='" + str(i) + "'"
            cursor = conn.execute(q1)
            for row in cursor:
                if (row[0] != None):
                    filtered_sentence1[index] = row[0]
            outtext1 = outtext1 + str(filtered_sentence1[index]) + ' '

        for index2,j in enumerate(filtered_sentence2):
            q2 = "SELECT WORD1 FROM WORDTB WHERE WORD1='" + str(j) + "' OR WORD2='" + str(j) + "' OR WORD3='" + str(j) + "' OR WORD4='" + str(j) + "' OR WORD5='" + str(j) + "'"
            cursor1 = conn.execute(q2)
            for row in cursor1:
                if (row[0] != None):
                    filtered_sentence2[index2] = row[0]
            outtext2 = outtext2 + str(filtered_sentence2[index2]) + ' '
			
#Creating ngrams for calculating Jaccard similarity
        Jbigrams1 = set(ngrams(filtered_sentence1,2))
        Jbigrams2 = set(ngrams(filtered_sentence2,2))
        Jtrigrams1 = set(ngrams(filtered_sentence1,3))
        Jtrigrams2 = set(ngrams(filtered_sentence2,3))
#Creating ngrams for calculating Cosine similarity
        Cbigrams1 = ngrams(filtered_sentence1,2)
        Cbigrams2 = ngrams(filtered_sentence2,2)
        Ctrigrams1 = ngrams(filtered_sentence1,3)
        Ctrigrams2 = ngrams(filtered_sentence2,3)
#Calculating Jaccard similarity
        biinter = Jbigrams1.intersection(Jbigrams2)
        triinter = Jtrigrams1.intersection(Jtrigrams2)
        biunion = Jbigrams1.union(Jbigrams2)
        triunion = Jtrigrams1.union(Jtrigrams2)
        j2 = str(round((len(biinter)/len(biunion)),2))
        j3 = str(round((len(triinter)/len(triunion)),2))
#Calculating Cosine similarity
        v1,v2 = build_vector(Cbigrams1,Cbigrams2)
        v3,v4 = build_vector(Ctrigrams1,Ctrigrams2)
        c2 = str(round((vector_cos5(v1,v2)),2))
        c3 = str(round((vector_cos5(v3,v4)),2))
#outtext1 = outtext1 + remove_prathya(str(i)) + ' '

        self.textEdit.setPlainText(outtext1)
        self.textEdit_2.setPlainText(outtext2)

        self.lineEdit.setText(j2)
        self.lineEdit_2.setText(j3)
        self.lineEdit_3.setText(c2)
        self.lineEdit_4.setText(c3)
        conn.close()
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

