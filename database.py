import pyodbc

class Database:
	def __init__(self, server='DESKTOP-ALESSIA' , username='ALESSIA', password='database', database='TEST', table_name='FILM'):
		self.server = server
		self.database = database
		self.username = username
		self.password = password
		self.table_name = table_name
		self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
		self.cursor = self.cnxn.cursor()


	def select_record(self, search_by, record):
		reply = []
		self.cursor.execute("SELECT * from " + self.table_name + " where "+ search_by + " = ?", record)
		for row in self.cursor.fetchall():
			reply.append(row)
		return reply

	def insert_record(self, record):	
		count = self.cursor.execute("SELECT COUNT(*) from " + self.table_name + " where TITOLO = ? and HARD_DISK = ? ", record[0], record[2]).fetchone()[0]
		if count == 0:
			self.cursor.execute("INSERT into " + self.table_name + " VALUES (?,?,?,?)", record[0], record[1], record[2], record[3])
			self.cnxn.commit()
			reply = record[0] +' inserito sul database'
		else:
			reply = record[0] +' già presente sul database'
		return reply

	def update_record(self, column, name, value):
		self.cursor.execute("UPDATE " +self.table_name+ " SET "+ column +" = ? WHERE TITOLO = ? ", value, name)
		self.cnxn.commit()
		return 'Record aggiornato correttamente'

	def delete_record(self, record):
		count = self.cursor.execute("SELECT COUNT(*) from " + self.table_name + " where TITOLO = ? AND LINGUA = ? and HARD_DISK = ? and ANNO = ?", record[0], record[1], record[2], record[3]).fetchone()[0]
		if count == 0:
			reply = record[0] + ' non è presente sul database'
		else:
			rep = input('Sono presenti ' + str(count) + ' records. Eliminare? Y/N  ')
			if rep == 'Y':	
				self.cursor.execute("DELETE from " + self.table_name + " WHERE TITOLO = ? AND LINGUA = ? and HARD_DISK = ? and ANNO = ?", record[0], record[1], record[2], record[3])
				self.cnxn.commit()
				reply = record[0] + ' eliminato'
			elif rep == 'N':
				reply = 'Il record non è stato eliminato'
			else:
				reply = 'Inserire "Y" oppure "N"'
		return reply

			

record = ['PROVA', 'nan', 'prova', '2019']
prova = Database()
