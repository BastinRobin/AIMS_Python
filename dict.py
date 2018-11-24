
people = [dict(name="Sakib", age=21, dept="MCA")
,dict(name="Deeraj", age=23, dept="MCA")
,dict(name="Boton", age=22, dept="MCA")
,dict(name="Abhishek", age=27, dept="MCA")
,dict(name="Gayathri", age=20, dept="MCA")
,dict(name="Subham", age=91, dept="MCA")]



# for person in people:
# 	print "========================"
# 	print person["name"], person['age'], person['dept']
# 	print "========================"

for i in range(len(people)):
	print people[i]["name"], people[i]["age"], people[i]["dept"]