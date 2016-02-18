#!Attendance1.py

def attend(attendances, date, students):
	attendances[date] = students
	return

attendances = dict([])
students = {"Seunghyun Lee", "Inyong Suh", "Jarang Seo", "Hyeongwoo Son", "Jeonghyun Han"}
attend(attendances,"150216",students)

print(attendances)


