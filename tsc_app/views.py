from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.conf import settings
import requests

# Create your views here.
def shows(request):
    
    url = 'http://localhost:8081/api/v1/shows'
    response = requests.get(url)
    data = response.json()
    
    
    context = {'results': data}
    return render(request, 'shows.html', context)
   
def show_characters(request, show_id):
    response = requests.get("http://localhost:8081/api/v1/shows/{}/characters".format(show_id))
    characters_data = response.json()

    context = {
        'characters': characters_data
    }
    return render(request, 'show_characters.html', context)

# def insert_shows(request):
#     return render(request,'insert_show.html')
# def insert_characters(request,show_id):
#     response = requests.post("http://localhost:8080/api/v1/shows/{}/characters".format(show_id))
#     if request.method=='POST':
#         id=request.POST['id']
#         name=request.POST['name']
#         description=request.POST['description']
#         tvShowId=request.POST['tvShowId']
#         context={'id':id,'name':name,'description':description,'tvShowId':tvShowId}
#         context.save()
#         return HttpResponse("Data Saved")
    
#     return render(request,'insert_char.html',context)