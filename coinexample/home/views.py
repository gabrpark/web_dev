from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "base.html", {})

# def price(request):
#     response = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
#     , headers = {"X-CMC_PRO_API_KEY": "6550f02e-d700-4dff-8cec-4753b7595770"
#     ,
#     })
#     data = response.json()
#     print(data)
#     return render(request, '/home.html', {
#         'id': data['id'],
#         'symbol': data['symbol']
#     })
