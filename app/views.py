from django.shortcuts import render

import datetime
import calendar

# Create your views here.
def index(request):
    if request.method == "POST":
        #username = request.POST['uname']
        #password = request.POST['psw']
        #print(username, password)
        date = request.POST['date']
        day = request.POST['day']
        val = dateCreator(date)
        cal = findDay(val)
        print(cal)
    return render(request, "index.html")

        # Python program to Find day of
# the week for a given date

def dateCreator(date):
     temp = date.split("/")
     string = temp[2] + temp[1] +  temp[0]
     return string

def findDay(date):
	born = datetime.datetime.strptime(date, '%d:%m:%Y').weekday()
    
	return (calendar.day_name[born])

# Driver program