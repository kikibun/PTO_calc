#PTO Calculator
import datetime
import sys

def current_pto(year, month, day):
    date = datetime.date(year, month, day)
    initial_pto = 62.61
    start_date = datetime.date(2017, 4, 8)
    # add PTO to bank - accrue 7.12 hours every 2 weeks
    acc_time = date - start_date
    acc_instance = acc_time.days // 14
    total_pto = (acc_instance * 7.12) + initial_pto
    print total_pto

current_pto(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
#       TEST        #
#future_date = datetime.date(2018, 4, 20)
#acc_future_time = future_date - start_date
#acc_future_instance = acc_future_time.days // 14
#future_pto = acc_future_instance * 7.12
#total_future_pto = future_pto + initial_pto
#print total_future_pto

# given a date, tally hours accrued since date (possible_PTO)

# subtract PTO manually
# given days of PTO desired, remove PTO hours (8 hrs / day) (taken_PTO)

# return leftover PTO hours
# use possible_PTO and taken_PTO to determine remaining_PTO
