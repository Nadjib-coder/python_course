from datetime import datetime


def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birthdate.year
    # - ((today.month, today.day) < (birthdate.month, birthdate.day)))
    print("You Age:", age)

calculate_age("2002-03-28")