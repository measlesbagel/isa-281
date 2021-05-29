#Cagle-Myles-HW

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import sqlite3

links = ['http://www.fsb.miamioh.edu/sambhack/students.txt','http://www.fsb.miamioh.edu/sambhack/courses.txt','http://www.fsb.miamioh.edu/sambhack/grades.txt']
dbs = ['students.db','courses.db','grades.db','studentgpa.db','coursegpa.db']
cursors = ['cur1','cur2','cur3']

conn1 = sqlite3.connect(dbs[0])
conn2 = sqlite3.connect(dbs[1])
conn3 = sqlite3.connect(dbs[2])
conn4 = sqlite3.connect(dbs[3])
conn5 = sqlite3.connect(dbs[4])
cur1 = conn1.cursor()
cur2 = conn2.cursor()
cur3 = conn3.cursor()
cur4 = conn4.cursor()
cur5 = conn5.cursor()

cur1.execute('drop table if exists students')
cur2.execute('drop table if exists courses')
cur3.execute('drop table if exists grades')
cur4.execute('drop table if exists studentgpa')
cur5.execute('drop table if exists coursegpa')

cur1.execute('create table students (sid integer, studentname text, primary key(sid))')
cur2.execute('create table courses (crn integer, coursename text, primary key(crn))')
cur3.execute('create table grades (sid integer, crn integer, grade integer, primary key(sid,crn))')
cur4.execute('create table studentgpa (sid, studentname, sgpa, primary key(sid))')
cur5.execute('create table coursegpa (crn, coursename, cgpa, primary key(crn))')

fhand1 = urllib.request.urlopen(links[0])
next(fhand1)
fhand2 = urllib.request.urlopen(links[1])
next(fhand2)
fhand3 = urllib.request.urlopen(links[2])
next(fhand3)

for lines in fhand1:
    part = lines.decode().rstrip().split('\t')
    sid = int(part[0])
    studentname = part[1]
    cur1.execute('''insert into students (sid, studentname)
    values(?,?)
    ''',(sid,studentname))
conn1.commit()

for lines in fhand2:
    part = lines.decode().rstrip().split('\t')
    crn = int(part[0])
    coursename = part[1]
    cur2.execute('''insert into courses (crn, coursename)
    values(?,?)
    ''',(crn,coursename))
conn2.commit()

for lines in fhand3:
    part = lines.decode().rstrip().split('\t')
    sid = int(part[0])
    crn = int(part[1])
    grades = part[2]
    cur3.execute('''insert into grades (sid, crn, grade)
    values(?,?,?)
    ''',(sid,crn,grades))
conn3.commit()

sgpastring1 = ('select sid, studentname from students')
sgpastring2 = ('select sid, avg(grade) from grades group by sid')

for row in cur1.execute(sgpastring1):
    cur4.execute('insert into studentgpa (sid, studentname) values(?,?)', (row[0],row[1]))
for row in cur3.execute(sgpastring2):
    cur4.execute('update studentgpa set sgpa = ? where sid = ?', (round(row[1],2),row[0]))

print('STUDENT GPA')
print('SID  Name  GPA')
for row in cur4.execute('select * from studentgpa order by sgpa desc'):
    print(row[0],row[1],row[2])
conn4.commit()

print('\n')

cgpastring1 = ('select crn, coursename from courses')
cgpastring2 = ('select crn, avg(grade) from grades group by crn')
for row in cur2.execute(cgpastring1):
    cur5.execute('insert into coursegpa (crn, coursename) values(?,?)',(row[0],row[1]))
for row in cur3.execute(cgpastring2):
    cur5.execute('update coursegpa set cgpa = ? where crn = ?', (round(row[1],2),row[0]))

print('COURSE GPA')
print('CRN Course Name GPA')    
for row in cur5.execute('select * from coursegpa order by crn asc'):
    print(row[0],row[1],row[2])
conn5.commit()

cur1.close()
cur2.close()
cur3.close()
cur4.close()
cur5.close()



