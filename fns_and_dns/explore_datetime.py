from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d"))

def calculate_future_date():
    days_to _add = int(input("Enter the number of days to add: "))
    today = datetime.now()
    future_date = today + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
def main():
        Display_current_datetime()
        Calculate_future_date()
        
       