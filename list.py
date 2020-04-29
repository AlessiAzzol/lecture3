import pyodbc
import pandas as pd

server = 'DESKTOP-ALESSIA' 
database = 'TEST' 
username = 'ALESSIA' 
password = 'database' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


def insert_all(table):	
	for row in table.values:
		count = cursor.execute("SELECT * from dbo.FILM where TITOLO = ? and HARD_DISK = ? ", str(row[0]), str(row[2])).rowcount
		if count == 0:
			cursor.execute("INSERT into dbo.FILM VALUES (?,?,?,?)", str(row[0]), str(row[1]), str(row[2]), str(row[3]))
			cnxn.commit()
			n = cursor.execute("SELECT * from dbo.FILM where TITOLO = ? and HARD_DISK = ? ", str(row[0]), str(row[2])).fetchone()[0]
			reply = 'E\' stato inserito '+str(n)
			print(reply)
		else:
			reply = str(row[0]) +' già presente sul database'
			print(reply)


table = pd.read_excel("C:\\Users\\azzol\\Dropbox\\Cartella pirata\\Film.xlsx")
insert_all(table)