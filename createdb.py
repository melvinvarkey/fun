#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:

	cur = con.cursor()
   	cur.execute("DROP TABLE IF EXISTS students")

	cur.execute("create table students (id int primary key auto_increment, name varchar(20), age int, gender varchar(10))")
	
