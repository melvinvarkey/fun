import MySQLdb
import sys

db = MySQLdb.connect('localhost', 'testuser', 'test623', 'testdb')

def showoption():
	print
	print "*" * 50
	print "\tStudent record"
	print "*" * 50 
	print
	print "\t1. View Records"
	print "\t2. Insert Student details"
	print "\t3. Update details"
	print "\t4. Delete Record"
	print "\t5. EXIT"
	print

def view():
	with db:	
		
		cur = db.cursor()
		cur.execute("select * from students")
		
		rows = cur.fetchall()
		print "#" * 50
		print
		for row in rows:
			print "\t",row[0],"\t",row[1],"\t\t",row[2],"\t",row[3]
		print
		print "#" * 50 
	showmenu()

def insert():
	name = raw_input("Name : ")
	age = raw_input("Age (below 20) : ")
	gender = raw_input("Gender (male/female) : ")
	
	cursor = db.cursor()
	cursor.execute("insert into students (name,age,gender) values (%s,%s,%s)",(name,age,gender))	
	db.commit()
	print
	showmenu()

def update():
	with db:
		cur = db.cursor()
		idd = raw_input("Enter id: ")
		cur.execute("select * from students where id = %s" % idd)
		rows = cur.fetchall()
		for row in rows:	
			print "\t",row[0],"\t",row[1],"\t\t",row[2],"\t",row[3]
		na = raw_input("Update Name: ")
		ag = raw_input("Update Age: ")
		ge = raw_input("Gender: ")
		cur.execute("update students set name = %s where id = %s",(na,idd))
		cur.execute("update students set age = %s where id = %s",(ag,idd))
		cur.execute("update students set gender = %s where id = %s",(ge,idd))
		print "Numbers of rows updated", cur.rowcount
	showmenu()
	
def delete():
	with db:
		cur = db.cursor()
		idd = raw_input("Enter id to be deleted: ")
		cur.execute("delete from students where id = %s",(idd))
		print "Number of rows deleted",cur.rowcount
		print 
	showmenu()

def showmenu():
	
	showoption()
	print
	op = raw_input("Select Option: ")

	if int(op) == 1:
		view()
	
	elif int(op) == 2:
		insert()

	elif int(op) == 3:
		update()

	elif int(op) == 4:
		delete()
		
	elif int(op) == 5:
		pass
	
	else:	
		print
		print "Wrong Option \n Try Again!!!"
		print
		showmenu()

showmenu()
 
