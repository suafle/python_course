class Person(object):
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)

    def printfullname(self):
        return "%s %s" % (self.firstname, self.lastname)

class Student(Person):
    def __init__(self,firstname,lastname,subject):
        #super(Person,self).__init__(firstname,lastname)
        Person.__init__(self,firstname,lastname)
        self.subject = subject
    def printsubject(self):
        return str(self.subject)
    def printnamesubject(self):
        return 'Name: '+str(self.firstname)+' '+str(self.lastname)+', Subject: '+str(self.subject)

class Teacher(Person):
    def __init__(self,firstname,lastname,teaching):
        #super(Person,self).__init__(firstname,lastname)
        Person.__init__(self,firstname,lastname)
        self.teaching = teaching
    def printteaching(self):
        return str(self.teaching)
    def printnameteaching(self):
        return 'Name:'+str(self.firstname)+' '+str(self.lastname)+', Teaching: '+str(self.teaching)


a = Person('A','B')
print(a.printfullname())
b = Student('A','B','Astronomy')
print(b.printfullname())
print(b.printsubject())
print(b.printnamesubject())
c = Teacher('C','D','Python')
print(c.printfullname())
print(c.printteaching())
print(c.printnameteaching())

