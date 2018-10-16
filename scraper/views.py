from django.shortcuts import render
from scraper import SQLConnScrape


# Create your views here.
def home(request):
    name = 'Kevin'
    r = SQLConnScrape.scrape_date()
    org = r[0]
    loc = r[1]
    pos = r[2]
    date = r[3]
    b1 = r[4]
    b2 = r[5]
    args = {'myName': name,
            'myOrg': org,
            'myLoc': loc,
            'myPos': pos,
            'myDate': date,
            'myB1': b1,
            'myB2': b2
            }

    return render(request, 'scraper/home.html', args)
