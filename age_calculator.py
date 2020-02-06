from datetime import datetime
from datetime import date

def check_birthdate(year, month, day):
	# write code here
	today = date.today()
	if int(year) > int(today.year):
		return False
	elif int(year) == int(today.year):
		if int(month) > int(today.month):
			return False
		elif int(month) == int(today.month):
			if int(day) > int(today.day):
				return False
			else:
				return True
		else:
			return True
	else:
		return True

def calculate_age(year, month, day):
	today = date.today()
	ans = (int(today.year) - int(year)) + ((int(today.month) - int(month))/12) + ((int(today.day) - int(day))/365)
	print ("you are "+str(int(ans//1))+"years old")

def main():
	# write main code here
	today = date.today()
	y1 = input("Enter year of birth: ")
	m1 = input("Enter month of birth: ")
	d1 = input("Enter day of birth: ")
	if check_birthdate(y1, m1, d1):
		calculate_age(y1, m1, d1)
	else :
		print ("the birthdate is invalid.")







if __name__ == '__main__':
	main()
