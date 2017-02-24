from django.shortcuts import render, redirect, HttpResponse
import datetime, random


def index(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
    return render(request, "gold/index.html")

def process(request):

    if request.method == "POST":
        now = datetime.datetime.now()
        locations = {
            "farm": random.randint(10, 20),
    		"cave": random.randint(5, 10),
    		"house": random.randint(2, 5),
    		"casino": random.randint(-50, 50)
        }

        for key, value in locations.iteritems():
            if request.POST['building'] == key:
                if locations[key] < 0:
                    gold = locations[key] * -1
                    message = "lost " + str(gold) + " gold coins at the " + key + " "
                    request.session['activities'].append(message + "|| " + str( now)))
                    request.session['gold_count'] -= gold
                else:
                    gold = locations[key]
                    message = "won " + str(gold) + " gold coins at the " + key + " "
                    request.session['activities'].append(message + "|| " + str( now)))
                    request.session['gold_count'] += gold

        #
        # if request.POST['building'] =="farm":
        #     message = "won" + str(locations['farm']) + " gold coins at the farm"
        #     request.session['activities'].append(message)
        #     request.session['gold_count'] += locations['farm']
        #
        # if request.POST['building'] =="cave":
        #     message = "won " + str(locations['cave']) + " gold coins at the cave"
        #     request.session['activities'].append(message)
        #     request.session['gold_count'] += locations['cave']
        #
        # if request.POST['building'] =="house":
        #     message = "won " + str(locations['house']) + " gold coins at the house!"
        #     request.session['activities'].append(message)
        #     request.session['gold_count'] += locations['house']
        #
        # if request.POST['building'] =="casino":
        #     if locations['casino'] < 0:
        #         message = "lost " + str(locations['casino']) + " gold coins at the casino!"
        #         request.session['activities'].append(message)
        #         request.session['gold_count'] = request.session['gold_count'] - locations['casino']
        #     else:
        #         message = "won " + str(locations['casino']) + " gold coins at the casino!"
        #         request.session['activities'].append(message)
        #         request.session['gold_count'] += locations['casino']

    return render(request, "gold/index.html", locations)
