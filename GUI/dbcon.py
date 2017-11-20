import sqlite3

conn = sqlite3.connect('../Test/synDb.db')
print ("Opened database successfully");

##conn.execute('''CREATE TABLE WORDTB
##       (ID INT PRIMARY KEY     NOT NULL,
##        WORD1          CHAR(75)    NOT NULL,
##   WORD2    CHAR(75),WORD3    CHAR(75),WORD4    CHAR(75),WORD5    CHAR(75));''')
##print ("Table1 created successfully");

##conn.execute('''CREATE TABLE SYNTB
##       (WORD1ID INT NOT NULL,
##       WORD2ID INT NOT NULL,
##       PRIMARY KEY (WORD1ID,WORD2ID));''')
##print ("Table2 created successfully");
#conn.execute("INSERT INTO WORDTB (ID,WORD1,WORD2,WORD3,WORD4) VALUES (1, 'අම්මා','මව','මෑණියෝ','මෑණි')");
#conn.commit()
cursor = conn.execute("SELECT WORD1 FROM WORDTB WHERE WORD1= 'මෑණි' OR WORD2 = 'මෑණි' OR WORD3 = 'මෑණි' OR WORD4= 'මෑණි'")
for row in cursor:
   #print ("ID = ", row[0])
   print ("WORD = ", row[0])
##   print ("WORD = ", row[2])
##   print ("WORD = ", row[3])
##   print ("WORD = ", row[4], "\n")

conn.close()
