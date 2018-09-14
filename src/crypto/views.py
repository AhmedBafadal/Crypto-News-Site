from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    #grab crypto price data
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,EOS,DASH,ETC,BCH,XRP,LTC&tsyms=USD,EUR')
    # print(dir(price_request))
    price = json.loads(price_request.content)


    #grab crypto news
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')


    #convert to json
    api = json.loads(api_request.content)
    return render(request, 'home.html',{'api':api, 'price':price})

def prices(request):
    if request.method=='POST':
        # print(dir(request.method))
        quote = request.POST['quote']
        quote = quote.upper().strip()
        # print(dir(request.POST['quote']))
        crypto_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+ quote+'&tsyms=USD,EUR')
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html',{'quote':quote, 'crypto':crypto})
    else:
        notfound = 'N/A'
        return render(request, 'prices.html',{'notfound':notfound})
        