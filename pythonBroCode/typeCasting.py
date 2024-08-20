name = "Lorenzo Taborda Frozza"
age = 19
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)
age = str(age)
age += "1"
print(age)
name = bool(name)
print(name) #i can use to check if there is a name, cause if it returns false i know that there isn't a name
