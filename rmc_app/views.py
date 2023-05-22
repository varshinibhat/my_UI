from django.shortcuts import render,HttpResponse,redirect
from django.conf import settings
import requests
# Create your views here.
def index(request):
    #response=requests.get('https://api.covid19api.com/countries').json()
    return render(request,'index.html')
    
def search_view(request):
    
    query = request.GET.get('q', '')
    #query="rick"
    #response = requests.get(f'https://rickandmortyapi.com/api/character/?name={query}')
    response = requests.get(f'http://localhost:8050/api/v1/characters/?name={query}')
    print("==================")
    print(response)
    if response.status_code==200:
        data = response.json()['characters'] # Extract the character data from the API response
    else:
        data=None
    context = {'query': query, 'results': data}
    #return render(request, 'search.html',{'response':response})
    return render(request, 'search.html', context)














# def my_view(request):
    
#     api_url = settings.API_URL
#     context = {'api_url': api_url}
#     return render(request, 'my_template.html', context)

# def sec(request):
#     return render(request,"sec.html")
# def my_view(request):
#     query="rick"
#     url = 'http://localhost:8080/api/v1/characters/?name={query}'
#     response = requests.get(url)
#     data = response.json()['results'] # Extract the character data from the API response
#     context = { 'results': data}
#     return render(request, 'search.html', context)
#     #return render(request, 'my_template.html', context)


#docker run -p 1500:5432 faizan10933/tvshowdb:1.0
#docker run -p 8080:8080 faizan10933/rmc:1.0 