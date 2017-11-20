import sqlite3
import codecs

conn = sqlite3.connect('../Test/synDb.db')
print ("Opened database successfully");

f = codecs.open('lemmadata.txt','r','utf_8')
x = f.read()
y = str(x).splitlines()
for i in y:
    string = str(i)
    words = string.split(',')
    print (words[0])
    print (words[1])
    cursor = conn.execute("SELECT max(ID) FROM LEMMATB")
    for row in cursor:
        wid = int(row[0])+1
        print (wid)
    conn.execute("INSERT INTO LEMMATB (ID,WORD,LEMMA) SELECT ?,?,? WHERE NOT EXISTS(SELECT 1 FROM LEMMATB WHERE WORD = ? AND LEMMA = ?)",(wid,words[0],words[1],words[0],words[1]))
    conn.commit()
conn.close()
        
    
