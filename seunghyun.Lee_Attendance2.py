#!Attendance2.py
import datetime, time, re

class Student:
        def __init__(self,name):
                if name == None:
                        raise Exception('Name is None')
                elif type(name) != str:
                        raise Exception('Name type is not string')
                else:
                        self.name = name
        def __str__(self):
                return self.name

class Attendance:
        attendList = dict([])

        def dataValidationCheck(func):
                def dateStringFormatCheck(date):
                        dateFormatChecker = re.compile(r"^(\d{2,4})-(\d{2})-(\d{2})$")
                        yymmdd = dateFormatChecker.match(date)
                        
                        if yymmdd == None:
                                return False

                        mm = yymmdd.group(2)            
                        mmChecker = re.match(r"(0\d)|(1[0-2])",mm)

                        if mmChecker == None:
                                return False
                        
                        dd = yymmdd.group(3)
                        ddChecker = re.match(r"([0-2]\d)|(3[0-1])",dd)

                        if ddChecker == None:
                                return False
                        else:
                                return True
                def wrapper(self, *args, **kwargs):
                        date = kwargs.get('date')

                        if type(date) == datetime.date:
                                kwargs['date'] = date.strftime('%y-%m-%d')
                        elif type(date) == str:                         
                                if not dateStringFormatCheck(date):
                                        raise Exception("Unvalid Date Format")
                        elif date == None:
                                kwargs['date'] = datetime.date.today().strftime('%y-%m-%d')
                        else:
                                raise Exception('Unvalid Date Type')

                        for s in args:
                                if (type(s) != list and type(s) != Student) and (type(s) != list) :
                                        #print("Argument type : " + type(s))
                                        raise Exception("Not valid argument type")

                        return func(self, *args, **kwargs)
                return wrapper

        @dataValidationCheck
        def attend(self,*args,**kwargs):
                date = kwargs.get('date')
                students = []
                for st in args:
                        students.append(st)
                print(date)
                if self.attendList.get(date) == None:
                        self.attendList[date] = set(students)
                else:
                        self.attendList[date].union(set(students))

        def list(self):
                print(self.attendList)

def makeStudentsFromText(*args):
        studentsList = []
        for name in args:
                if type(name) == str:
                        studentsList.append(Student(name))

        return studentsList

myFirstAttendance = Attendance()

todayStudents=(Student("Seunghyun Lee"), Student("abc"), Student("def"), Student("ghi"))
student1 = Student("shlee")

print(type(todayStudents))

myFirstAttendance.attend(student1,date=None)

myFirstAttendance.list()

