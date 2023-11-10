## UTILITY
def get_today_date_string(self):
	today = datetime.date.today()
	date_string = today.strftime("%Y%m%d")
	print(date_string) # debug
	return date_string