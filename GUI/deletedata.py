import sqlite3

conn = sqlite3.connect('../Test/synDb.db')
print ("Opened database successfully");

conn.execute("DELETE FROM WORDTB WHERE WORD1 = 'අහස' ")
#conn.execute("DELETE FROM LEMMATB WHERE WORD = 'පිරිසක්' ")
conn.commit()
conn.close()
