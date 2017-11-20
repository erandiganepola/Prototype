# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProcessUi3.ui'
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
        Form.resize(657, 662)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 360, 111, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.line11 = QtGui.QLineEdit(Form)
        self.line11.setGeometry(QtCore.QRect(190, 420, 80, 20))
        self.line11.setObjectName(_fromUtf8("line11"))
        self.line13 = QtGui.QLineEdit(Form)
        self.line13.setGeometry(QtCore.QRect(390, 420, 80, 20))
        self.line13.setObjectName(_fromUtf8("line13"))
        self.textEdit_2 = QtGui.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(335, 30, 315, 321))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 390, 81, 31))
        self.label.setLineWidth(1)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(290, 390, 81, 31))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line12 = QtGui.QLineEdit(Form)
        self.line12.setGeometry(QtCore.QRect(290, 420, 80, 20))
        self.line12.setObjectName(_fromUtf8("line12"))
        self.line14 = QtGui.QLineEdit(Form)
        self.line14.setGeometry(QtCore.QRect(490, 420, 80, 20))
        self.line14.setObjectName(_fromUtf8("line14"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(390, 390, 81, 31))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(490, 390, 81, 31))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(130, 10, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(470, 10, 71, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 315, 321))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 360, 111, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(140, 450, 81, 20))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(140, 480, 81, 20))
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(120, 540, 81, 20))
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(120, 510, 81, 20))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(140, 420, 31, 20))
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(110, 600, 81, 20))
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(120, 570, 81, 20))
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.line24 = QtGui.QLineEdit(Form)
        self.line24.setGeometry(QtCore.QRect(490, 450, 80, 20))
        self.line24.setObjectName(_fromUtf8("line24"))
        self.line21 = QtGui.QLineEdit(Form)
        self.line21.setGeometry(QtCore.QRect(190, 450, 80, 20))
        self.line21.setObjectName(_fromUtf8("line21"))
        self.line23 = QtGui.QLineEdit(Form)
        self.line23.setGeometry(QtCore.QRect(390, 450, 80, 20))
        self.line23.setObjectName(_fromUtf8("line23"))
        self.line22 = QtGui.QLineEdit(Form)
        self.line22.setGeometry(QtCore.QRect(290, 450, 80, 20))
        self.line22.setObjectName(_fromUtf8("line22"))
        self.line64 = QtGui.QLineEdit(Form)
        self.line64.setGeometry(QtCore.QRect(490, 570, 80, 20))
        self.line64.setObjectName(_fromUtf8("line64"))
        self.line61 = QtGui.QLineEdit(Form)
        self.line61.setGeometry(QtCore.QRect(190, 570, 80, 20))
        self.line61.setObjectName(_fromUtf8("line61"))
        self.line63 = QtGui.QLineEdit(Form)
        self.line63.setGeometry(QtCore.QRect(390, 570, 80, 20))
        self.line63.setObjectName(_fromUtf8("line63"))
        self.line62 = QtGui.QLineEdit(Form)
        self.line62.setGeometry(QtCore.QRect(290, 570, 80, 20))
        self.line62.setObjectName(_fromUtf8("line62"))
        self.line34 = QtGui.QLineEdit(Form)
        self.line34.setGeometry(QtCore.QRect(490, 480, 80, 20))
        self.line34.setObjectName(_fromUtf8("line34"))
        self.line31 = QtGui.QLineEdit(Form)
        self.line31.setGeometry(QtCore.QRect(190, 480, 80, 20))
        self.line31.setObjectName(_fromUtf8("line31"))
        self.line33 = QtGui.QLineEdit(Form)
        self.line33.setGeometry(QtCore.QRect(390, 480, 80, 20))
        self.line33.setObjectName(_fromUtf8("line33"))
        self.line32 = QtGui.QLineEdit(Form)
        self.line32.setGeometry(QtCore.QRect(290, 480, 80, 20))
        self.line32.setObjectName(_fromUtf8("line32"))
        self.line44 = QtGui.QLineEdit(Form)
        self.line44.setGeometry(QtCore.QRect(490, 510, 80, 20))
        self.line44.setObjectName(_fromUtf8("line44"))
        self.line41 = QtGui.QLineEdit(Form)
        self.line41.setGeometry(QtCore.QRect(190, 510, 80, 20))
        self.line41.setObjectName(_fromUtf8("line41"))
        self.line43 = QtGui.QLineEdit(Form)
        self.line43.setGeometry(QtCore.QRect(390, 510, 80, 20))
        self.line43.setObjectName(_fromUtf8("line43"))
        self.line42 = QtGui.QLineEdit(Form)
        self.line42.setGeometry(QtCore.QRect(290, 510, 80, 20))
        self.line42.setObjectName(_fromUtf8("line42"))
        self.line54 = QtGui.QLineEdit(Form)
        self.line54.setGeometry(QtCore.QRect(490, 540, 80, 20))
        self.line54.setObjectName(_fromUtf8("line54"))
        self.line51 = QtGui.QLineEdit(Form)
        self.line51.setGeometry(QtCore.QRect(190, 540, 80, 20))
        self.line51.setObjectName(_fromUtf8("line51"))
        self.line53 = QtGui.QLineEdit(Form)
        self.line53.setGeometry(QtCore.QRect(390, 540, 80, 20))
        self.line53.setObjectName(_fromUtf8("line53"))
        self.line52 = QtGui.QLineEdit(Form)
        self.line52.setGeometry(QtCore.QRect(290, 540, 80, 20))
        self.line52.setObjectName(_fromUtf8("line52"))
        self.line74 = QtGui.QLineEdit(Form)
        self.line74.setGeometry(QtCore.QRect(490, 600, 80, 20))
        self.line74.setObjectName(_fromUtf8("line74"))
        self.line71 = QtGui.QLineEdit(Form)
        self.line71.setGeometry(QtCore.QRect(190, 600, 80, 20))
        self.line71.setObjectName(_fromUtf8("line71"))
        self.line73 = QtGui.QLineEdit(Form)
        self.line73.setGeometry(QtCore.QRect(390, 600, 80, 20))
        self.line73.setObjectName(_fromUtf8("line73"))
        self.line72 = QtGui.QLineEdit(Form)
        self.line72.setGeometry(QtCore.QRect(290, 600, 80, 20))
        self.line72.setObjectName(_fromUtf8("line72"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Process text", None))
        self.pushButton.setText(_translate("Form", "Process", None))
        self.label.setText(_translate("Form", "Jaccard-Bigrams", None))
        self.label_2.setText(_translate("Form", "Jaccard-Trigrams", None))
        self.label_3.setText(_translate("Form", "Cosine-Bigrams", None))
        self.label_4.setText(_translate("Form", "Cosine-Trigrams", None))
        self.label_5.setText(_translate("Form", "Document 1", None))
        self.label_6.setText(_translate("Form", "Document 2", None))
        self.pushButton_2.setText(_translate("Form", "Clear", None))
        self.label_7.setText(_translate("Form", "LEM", None))
        self.label_8.setText(_translate("Form", "SYR", None))
        self.label_9.setText(_translate("Form", "STR + SYR", None))
        self.label_10.setText(_translate("Form", "STR + LEM", None))
        self.label_11.setText(_translate("Form", "STR", None))
        self.label_12.setText(_translate("Form", "STR+LEM+SYR", None))
        self.label_13.setText(_translate("Form", "LEM + SYR", None))
        self.pushButton.clicked.connect(self.buttonProcessClick)
        self.pushButton_2.clicked.connect(self.buttonClearClick)

    def buttonClearClick(self):
        self.textEdit.clear()
        self.textEdit_2.clear()

        self.line11.clear()
        self.line12.clear()
        self.line13.clear()
        self.line14.clear()
        self.line21.clear()
        self.line22.clear()
        self.line23.clear()
        self.line24.clear()
        self.line31.clear()
        self.line32.clear()
        self.line33.clear()
        self.line34.clear()
        self.line41.clear()
        self.line42.clear()
        self.line43.clear()
        self.line44.clear()
        self.line51.clear()
        self.line52.clear()
        self.line53.clear()
        self.line54.clear()
        self.line61.clear()
        self.line62.clear()
        self.line63.clear()
        self.line64.clear()
        self.line71.clear()
        self.line72.clear()
        self.line73.clear()
        self.line74.clear()

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
        punct = set(stopwords.words("punct"))
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
#removing puntuations        
        punrem_sentence1 = [w1 for w1 in words1 if not w1 in punct]
        punrem_sentence2 = [w2 for w2 in words2 if not w2 in punct]
        punremcopy1 = punrem_sentence1.copy()
        punremcopy2 = punrem_sentence2.copy()
#removing stopwords        
        stwrem_sentence1 = [w1 for w1 in punrem_sentence1 if not w1 in sinstopwords]
        stwrem_sentence2 = [w2 for w2 in punrem_sentence2 if not w2 in sinstopwords]
        strmcopy1 = stwrem_sentence1.copy()
        strmcopy2 = stwrem_sentence2.copy()

        	
        outtext1 = ''
        outtext2 = ''
#Lemmatization
        def Lemmatization(wordlist):          
            for index3,i in enumerate(wordlist):
                q1 = "SELECT LEMMA FROM LEMMATB WHERE WORD='" + str(i) + "'"
                cursor = conn.execute(q1)
                for row in cursor:
                    if (row[0] != None):
                        wordlist[index3] = row[0]
            return wordlist
#Synonym recognition
        def synrecog(wordlist):
            for index,i in enumerate(wordlist):
                q1 = "SELECT WORD1 FROM WORDTB WHERE WORD1='" + str(i) + "' OR WORD2='" + str(i) + "' OR WORD3='" + str(i) + "' OR WORD4='" + str(i) + "' OR WORD5='" + str(i) + "'"
                cursor = conn.execute(q1)
                for row in cursor:
                    if (row[0] != None):
                        wordlist[index] = row[0]
            return wordlist
            #outtext1 = outtext1 + str(filtered_sentence1[index]) + ' '
            #outtext2 = outtext2 + str(filtered_sentence2[index2]) + ' '
			
#Creating ngrams for calculating Jaccard similarity
        def Jngrams(wordlist,num):
            Jngram = set(ngrams(wordlist,num))
            return Jngram
#Creating ngrams for calculating Cosine similarity
        def Cngrams(wordlist,num):
            Cngram = ngrams(wordlist,num)
            return Cngram
#Calculating Bigram Jaccard similarity
        def BiJaccard(wordlist,wordlist2):
            biinter = Jngrams(wordlist,2).intersection(Jngrams(wordlist2,2))
            biunion = Jngrams(wordlist,2).union(Jngrams(wordlist2,2))
            j2 = str(round((len(biinter)/len(biunion)),2))
            return j2
#Calculating Trigram Jaccard similarity
        def TriJaccard(wordlist,wordlist2):
            triinter = Jngrams(wordlist,3).intersection(Jngrams(wordlist2,3))
            triunion = Jngrams(wordlist,3).union(Jngrams(wordlist2,3))
            j3 = str(round((len(triinter)/len(triunion)),2))
            return j3
#Calculating Bigram Cosine similarity
        def BiCosine(wordlist,wordlist2):
            v1,v2 = build_vector(Cngrams(wordlist,2),Cngrams(wordlist2,2))
            c2 = str(round((vector_cos5(v1,v2)),2))
            return c2
#Calculating Bigram Cosine similarity
        def TriCosine(wordlist,wordlist2):
            v3,v4 = build_vector(Cngrams(wordlist,3),Cngrams(wordlist2,3))
            c3 = str(round((vector_cos5(v3,v4)),2))
            return c3

#Calculating & Setting stopword remove only
        self.line11.setText(BiJaccard(stwrem_sentence1,stwrem_sentence2))
        self.line12.setText(TriJaccard(stwrem_sentence1,stwrem_sentence2))
        self.line13.setText(BiCosine(stwrem_sentence1,stwrem_sentence2))
        self.line14.setText(TriCosine(stwrem_sentence1,stwrem_sentence2))
            
#Calculating & setting lemmatization only
        lem1 = Lemmatization(punrem_sentence1)
        lem2 = Lemmatization(punrem_sentence2)
        self.line21.setText(BiJaccard(lem1,lem2))
        self.line22.setText(TriJaccard(lem1,lem2))
        self.line23.setText(BiCosine(lem1,lem2))
        self.line24.setText(TriCosine(lem1,lem2))

#Calculating & setting synonym recog only
        sym1 = synrecog(punremcopy1)
        sym2 = synrecog(punremcopy2)
        self.line31.setText(BiJaccard(sym1,sym2))
        self.line32.setText(TriJaccard(sym1,sym2))
        self.line33.setText(BiCosine(sym1,sym2))
        self.line34.setText(TriCosine(sym1,sym2))

#Calculating & setting stopword remove & Lemmatization
        stlem1 = Lemmatization(stwrem_sentence1)
        stlem2 = Lemmatization(stwrem_sentence2)
        self.line41.setText(BiJaccard(stlem1,stlem2))
        self.line42.setText(TriJaccard(stlem1,stlem2))
        self.line43.setText(BiCosine(stlem1,stlem2))
        self.line44.setText(TriCosine(stlem1,stlem2))

#Calculating & setting stopword remove & synonym recog
        stsyn1 = synrecog(strmcopy1)
        stsyn2 = synrecog(strmcopy2)
        self.line51.setText(BiJaccard(stsyn1,stsyn2))
        self.line52.setText(TriJaccard(stsyn1,stsyn2))
        self.line53.setText(BiCosine(stsyn1,stsyn2))
        self.line54.setText(TriCosine(stsyn1,stsyn2))

#Calculating & setting lemmatization & synonym recog
        lemsyn1 = synrecog(lem1)
        lemsyn2 = synrecog(lem2)
        self.line61.setText(BiJaccard(lemsyn1,lemsyn2))
        self.line62.setText(TriJaccard(lemsyn1,lemsyn2))
        self.line63.setText(BiCosine(lemsyn1,lemsyn2))
        self.line64.setText(TriCosine(lemsyn1,lemsyn2))

#Calculating & setting stopword rem + lemma + syn recog
        stlemsyn1 = synrecog(stlem1)
        stlemsyn2 = synrecog(stlem2)
        self.line71.setText(BiJaccard(stlemsyn1,stlemsyn2))
        self.line72.setText(TriJaccard(stlemsyn1,stlemsyn2))
        self.line73.setText(BiCosine(stlemsyn1,stlemsyn2))
        self.line74.setText(TriCosine(stlemsyn1,stlemsyn2))

        for i in stlemsyn1:
            outtext1 = outtext1 + str(i) + ' '
        for j in stlemsyn2:
            outtext2 = outtext2 + str(j) + ' '

        self.textEdit.setPlainText(outtext1)
        self.textEdit_2.setPlainText(outtext2)
        conn.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

