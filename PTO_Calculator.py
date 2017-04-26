#PTO Calculator
import datetime
import sys

vacation = {datetime.date(2017, 10, 6): 5, datetime.date(2017, 6, 7): 7, datetime.date(2017, 8, 2): 3}

request = raw_input('Date of Interest (Y, M, D): ')
pieces = request.split()
year = int(pieces[0])
month = int(pieces[1])
day = int(pieces[2])
#print year, month, day
days = raw_input('How many days off?: ')

def current_pto(year, month, day):
    date = datetime.date(year, month, day)
    initial_pto = 62.61
    start_date = datetime.date(2017, 4, 8)
    # add PTO to bank - accrue 7.12 hours every 2 weeks
    acc_time = date - start_date
    acc_instance = acc_time.days // 14
    total_pto = (acc_instance * 7.12) + initial_pto
    #print total_pto
    return total_pto

try:
    current_pto(year, month, day)
except:
    print 'BAD'

#       TEST        #
#future_date = datetime.date(2018, 4, 20)
#acc_future_time = future_date - start_date
#acc_future_instance = acc_future_time.days // 14
#future_pto = acc_future_instance * 7.12
#total_future_pto = future_pto + initial_pto
#print total_future_pto

# given days of PTO desired, remove PTO hours (8 hrs / day) (taken_PTO)
# return leftover PTO hours
# use possible PTO and taken PTO to determine remaining PTO
def left_pto(days):
    total_pto = current_pto(year, month, day)
    if days == '':
        days = 0
    for i in vacation.keys():
        if datetime.date(year, month, day) > i:
            days += vacation[i]
    hours_taken = int(days) * 8
    pto_remain = total_pto - hours_taken
    print 'You will have accrued %s hours of pto.' %(total_pto)
    print 'After your days off, you will have %s hours left.' %(pto_remain)

try:
    left_pto(days)
except:
    print 'NUMBERS ONLY'
    raise
# subtract PTO manually