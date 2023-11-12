from datetime import datetime

now = datetime.now()
today = datetime.today()

print("The current date and time is:", now)
print("The current date and time is:", today)

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

date_str = "2023-11-12 12:46:19"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("pared_date", parsed_date)