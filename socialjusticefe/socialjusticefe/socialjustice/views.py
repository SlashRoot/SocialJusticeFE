from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.
def frontend(request):
    r = requests.get('http://wikipaltz.org/wiki/Events')
    soup = BeautifulSoup(r.text)
    
    time = str(soup.find(id='mw-content-text').get_text())
    

    return render(request, 'test.html', locals())
