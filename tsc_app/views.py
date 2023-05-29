from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.conf import settings
import requests

# Create your views here.
def shows(request):
    
    url = 'http://localhost/tsc/shows'
    response = requests.get(url)
    data = response.json()
    
    
    context = {'results': data}
    return render(request, 'shows.html', context)
   
def show_characters(request, show_id):
    response = requests.get("http://localhost/tsc/shows/{}/characters".format(show_id))
    characters_data = response.json()

    context = {
        'characters': characters_data
    }
    return render(request, 'show_characters.html', context)

def insert_shows(request):
    if request.method=='POST':

        data_to_update={
        'id': int(request.POST.get('id')),
        'title': request.POST.get('title'),
        'synopsis': request.POST.get('synopsis'),
        'releaseYear': int(request.POST.get('releaseYear'))

        }

        #print("=================8888888888888888888")
        # print(title)

        api_url = 'http://localhost/tsc/shows'  # Replace with your API endpoint URL
        response = requests.post(api_url, json=data_to_update)

        if response.status_code == 200 or response.status_code==201:
        # Data successfully updated
            return HttpResponse('Data updated successfully')
        else:
        # Failed to update data
            #print("222222222222222222222222222222222")
            #print(response.status_code)
            return HttpResponse('Failed to update data')

    #  
    
    # print()

    return render(request,'insert_show.html')


    
def insert_characters(request,show_id):

    if request.method=='POST':

        data_to_update={
        'id': int(request.POST.get('id')),
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
         'tvShowId': int(request.POST.get('tvShowId'))

        }

        print("=================8888888888888888888")
        # print(title)

        api_url = 'http://localhost/tsc/shows/{}/characters".format(show_id)'  # Replace with your API endpoint URL
        response = requests.post(api_url, json=data_to_update)

        if response.status_code == 200 or response.status_code==201:
        # Data successfully updated
            return HttpResponse('Data updated successfully')
        else:
        # Failed to update data
            print("222222222222222222222222222222222")
            print(response.status_code)
            return HttpResponse('Failed to update data')

    #  
    
    # print()

    return render(request,'insert_char.html')
#     return render(request,'insert_char.html',context)

def insert_Tvcharacters(request):

    if request.method=='POST':
        tvShowId= int(request.POST.get('tvShowId'))

        data_to_update={
        'id': int(request.POST.get('id')),
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
         'tvShowId': int(request.POST.get('tvShowId'))

        }

        print("=================8888888888888888888")
        # print(title)

        api_url = 'http://localhost/tsc/shows/{}/characters'.format(tvShowId)  # Replace with your API endpoint URL
        response = requests.post(api_url, json=data_to_update)

        if response.status_code == 200 or response.status_code==201:
        # Data successfully updated
            return HttpResponse('Data updated successfully')
        else:
        # Failed to update data
            print("222222222222222222222222222222222")
            print(response.status_code)
            return HttpResponse('Failed to update data')

    #  
    
    # print()

    return render(request,'insert_char.html')