import sqlite3
import codecs

conn = sqlite3.connect('../Test/synDb.db')
print ("Opened database successfully");

f = codecs.open('syndata.txt','r','utf_8')
x = f.read()
y = str(x).splitlines()
for i in y:
    string = str(i)
    words = string.split(',')
    if (len(words) == 2):
        print (words[0])
        print (words[1])
        cursor = conn.execute("SELECT max(ID) FROM WORDTB")
        for row in cursor:
            wid = int(row[0])+1
            print (wid)
        conn.execute("INSERT INTO WORDTB (ID,WORD1,WORD2) SELECT ?,?,? WHERE NOT EXISTS(SELECT 1 FROM WORDTB WHERE WORD1 = ? AND WORD2 = ?)",(wid,words[0],words[1],words[0],words[1]))
        conn.commit()
    if (len(words) == 3):
        print (words[0])
        print (words[1])
        print (words[2])
        cursor = conn.execute("SELECT max(ID) FROM WORDTB")
        for row in cursor:
            wid = int(row[0])+1
            print (wid)
        conn.execute("INSERT INTO WORDTB (ID,WORD1,WORD2,WORD3) SELECT ?,?,?,? WHERE NOT EXISTS(SELECT 1 FROM WORDTB WHERE WORD1 = ? AND WORD2 = ? AND WORD3 = ?)",(wid,words[0],words[1],words[2],words[0],words[1],words[2]))
        conn.commit()
    if (len(words) == 4):
        print (words[0])
        print (words[1])
        print (words[2])
        print (words[3])
        cursor = conn.execute("SELECT max(ID) FROM WORDTB")
        for row in cursor:
            wid = int(row[0])+1
            print (wid)
        conn.execute("INSERT INTO WORDTB (ID,WORD1,WORD2,WORD3,WORD4) SELECT ?,?,?,?,? WHERE NOT EXISTS(SELECT 1 FROM WORDTB WHERE WORD1 = ? AND WORD2 = ? AND WORD3 = ? AND WORD4 = ?)",(wid,words[0],words[1],words[2],words[3],words[0],words[1],words[2],words[3]))
        conn.commit()
conn.close()
