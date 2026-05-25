from datetime import date
name = input("enter your name:")
current_year = date.today().year
birth_year,date,day = map(int,input("enter your birthday(yyyy-mm-dd):").split("-"))
age = current_year - birth_year
print(f" hello {name}! You are {age}. Good morning 😃")
