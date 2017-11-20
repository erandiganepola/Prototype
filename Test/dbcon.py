import sqlite3

conn = sqlite3.connect('synDb.db')
print ("Opened database successfully");

##conn.execute('''CREATE TABLE WORDTB
##       (ID INT PRIMARY KEY     NOT NULL,
##        WORD1          CHAR(75)    NOT NULL,
##   WORD2    CHAR(75),WORD3    CHAR(75),WORD4    CHAR(75),WORD5    CHAR(75));''')
##print ("Table1 created successfully");
##conn.execute('''CREATE TABLE LEMMATB
##       (ID INT PRIMARY KEY     NOT NULL,
##        WORD          CHAR(75)    NOT NULL,
##   LEMMA    CHAR(75)	NOT NULL);''')
##print ("Table1 created successfully");

##conn.execute('''CREATE TABLE SYNTB
##       (WORD1ID INT NOT NULL,
##       WORD2ID INT NOT NULL,
##       PRIMARY KEY (WORD1ID,WORD2ID));''')
##print ("Table2 created successfully");
#conn.execute("INSERT INTO LEMMATB (ID,WORD,LEMMA) VALUES (5,'කුඹුරට','කුඹුර')");
#conn.execute("INSERT INTO LEMMATB (ID,WORD,LEMMA) VALUES (6,'යති','යයි')");
#conn.execute("INSERT INTO LEMMATB (ID,WORD,LEMMA) VALUES (7,'උදලු','උදැල්ල')");
#conn.execute("INSERT INTO WORDTB (ID,WORD1,WORD2) VALUES (2,'ගොවියා','වගාකරු')"); 
#conn.commit()
print ("Inserted & commited successfully")
cursor = conn.execute("SELECT LEMMA FROM LEMMATB WHERE WORD= 'ගොවියන්ට'")
for row in cursor:
   #print ("ID = ", row[0])
   print ("WORD = ", row[0])
##   print ("WORD = ", row[2])
##   print ("WORD = ", row[3])
##   print ("WORD = ", row[4], "\n")

conn.close()
