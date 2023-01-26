from datetime import datetime

def check_date(year_end,month_end,day_end):

    # Current Year, Month and Day
    year = (int(datetime.now().strftime("%Y")))
    month = (int(datetime.now().strftime("%m")))
    day = (int(datetime.now().strftime("%d")))

    # Compare current date with end date
    if year > year_end or month >= month_end and day > day_end:
        return False
    else:
        return True
   
if __name__ == '__main__':
    
    day_end = 'Your Day'
    month_end = 'Your Month'
    year_end = 'Your Year'

    suscription = check_date(year_end,month_end,day_end)

    if suscription == False:
        print('Your suscription has ended.')
    else:
        print('Active subscription')
        #function that your app does
