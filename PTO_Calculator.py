#PTO Calculator
import datetime
import sys
import pickle

#vitual environment: create virtual environment called env - virtualenv env
# enter vitual env named env - . env/bin/activate

#vacation = {datetime.date(2017, 10, 6): 5, datetime.date(2017, 6, 7): 7, datetime.date(2017, 8, 2): 3}
vacation = {}
start_date = datetime.date(2017, 4, 8)
initial_pto = 62.61

def current_pto(date):
    global initial_pto, start_date
    # add PTO to bank - accrue 7.12 hours every 2 weeks
    acc_time = date - start_date
    acc_instance = acc_time.days // 14
    total_pto = (acc_instance * 7.12) + initial_pto
    #print total_pto
    return total_pto

def save_pto():
    global initial_pto, start_date
    initial_pto_dict = {"initial_pto_hours" : initial_pto, "initial_pto_date": start_date}
    with open("pto.txt","w") as file:
        file.write(pickle.dumps(initial_pto_dict))

def load_pto():
    global start_date, initial_pto
    with open("pto.txt","r") as file:
        contents = file.read()
        py_contents = pickle.loads(contents)
        print py_contents
        initial_pto = py_contents["initial_pto_hours"]
        start_date = py_contents["initial_pto_date"]
        #print py_contents["initial_pto"]

def add_vacation(vacation_date, days_off):
    vacation[vacation_date] = days_off

#load_pto()

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
def left_pto(date):
    total_pto = current_pto(date)
    days = 0
    for i in vacation.keys():
        if date >= i:
            days += vacation[i]
    hours_taken = days * 8
    pto_remain = total_pto - hours_taken
    #print 'You will have accrued %s hours of pto.' %(total_pto)
    return pto_remain

#store new dates in a file
def save_vacation_dates():
    global vacation
    with open("vacation.txt","w") as file:
        file.write(pickle.dumps(vacation))

def load_vacation_dates():
    global vacation
    with open("vacation.txt","r") as file:
        contents = file.read()
        py_contents = pickle.loads(contents)
        vacation = py_contents

def get_vacation_days():
    global vacation
    return vacation

def convert_date(date_given):
    pieces = date_given.split()
    year = int(pieces[0])
    month = int(pieces[1])
    day = int(pieces[2])
    return datetime.date(year, month, day)
    #print year, month, day

if __name__ == "__main__":
    try:
        load_vacation_dates()
    except IOError:
        print "NO VACATION FILE"
        exit(1)

    try:
        load_pto()
    except IOError:
        print "NO PTO FILE"
        exit(2)

    task = raw_input('What do you want to do?\n1. Add vacation\n2.View PTO\n3. Set new PTO start values\n4. View planned vacations\n5. Start server\n:')

    if task == '1':
        request = raw_input('Date of Interest (Y, M, D): ')
        date = convert_date(request)
        days = raw_input('How many days off?: ')
        days = int(days)
        add_vacation(date, days)
        pto_remain = left_pto(date)
        if pto_remain < 0:
            print "NOT ENOUGH HOURS"
            exit(3)
        print 'After your days off, you will have %s hours left.' %(pto_remain)
        confirm = raw_input('Confirm vacation Y/N: ')
        if confirm.lower() == 'y':
            save_vacation_dates()
            print 'VACATION SAVED'
        else:
            'VACATION NOT SAVED'
            exit(4)
    elif task == '2':
        request = raw_input('Date of Interest (Y, M, D): ')
        date = convert_date(request)
        try:
            current_pto(date)
        except:
            print 'BAD'
            raise
        try:
            pto_remain = left_pto(date)
            print 'After your days off, you will have %s hours left.' %(pto_remain)
        except:
            print 'NUMBERS ONLY'
            raise
    elif task == '3':
        new_start_date = raw_input('Enter new start date: ')
        new_start_hours = raw_input('Enter new start hours: ')
        date = convert_date(new_start_date)
        initial_pto = int(new_start_hours)
        start_date = date
        print 'NEW VALUES SAVED'
        save_pto()
    elif task == '4':
        vacay = get_vacation_days()
        print vacay
    elif task == '5':
        from flask import Flask
        app = Flask(__name__)
        @app.route("/current/")
        def flask_get_pto():
            date = datetime.date.today()
            #return current_pto(date)
            return datetime.date.today()
            return "test"
        app.run()
