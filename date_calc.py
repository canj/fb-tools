# This program is used to get the amount of money needed per day to fix any pacing issues

from datetime import date
from datetime import datetime


# Get campaign ending year from user
year = int(input('Campaign ending year: '))
month = int(input('Campaign ending month: '))
day = int(input('Campaign ending day: '))
campaign_end = date(year, month, day)
campaign_start = date.today()

# Calculate days between two dates
delta = campaign_end - campaign_start

# Get remaining budget 
print("How much money is left in this campaign?")
budget_remaining = input()

# Calculate daily spend
daily_spend = int(budget_remaining) / int(delta.days)
daily_spend = str(daily_spend)

# Print remaining days
print(delta.days)
print(budget_remaining)
print("Your daily spend should be $" + daily_spend)
