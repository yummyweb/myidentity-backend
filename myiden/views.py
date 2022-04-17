from django.shortcuts import render
import pyTigerGraph as tg
import json
import requests
import collections
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#x = tg.getToken("l69n326p9eavr7asdhrq6ubike8lk53e", setToken=True, lifetime=None)




def home(request):
    context_dict = {}
    return render(request, 'home.html', context_dict)


@csrf_exempt
def create_person(request):
    context_dict = {}
    #context_dict['problems'] = #
    #params = { 'id' : "5", 'place_of_birth': "Vizag", 'date_of_birth': "2-2-1998", 'profession': "doctor", 'spouse': "mary", 'age': 20, 'email': "peter@gmail.com", 'children' : "2"}
    
    id = request.POST.get('id', '')
    place_of_birth = request.POST.get('place_of_birth', '')
    date_of_birth = request.POST.get('date_of_birth', '')
    profession = request.POST.get('profession', '')
    spouse = request.POST.get('spouse', '')
    age = request.POST.get('age', '')
    email = request.POST.get('email', '')
    children = request.POST.get('children', '')
    
    params = { 'id' : id, 'place_of_birth': place_of_birth, 'date_of_birth': date_of_birth, 'profession': profession, 'spouse': spouse, 'age': age, 'email': email, 'children' : children}

    
    conn = tg.TigerGraphConnection(host="https://my-identity01.i.tgcloud.io/", graphname="myidentity", username="tigergraph", password="myidentity", apiToken="s7uv8j45pupb08ant6fen71fnpkn96jp")

    preInstalledResult = conn.runInstalledQuery("insertuser", params) 


    #json_object = json.loads(preInstalledResult[0]['gs'][0])
    #for i in preInstalledResult[0]['gs']:
     #   print(i)
    #for i in preInstalledResult:
    #    print(i)
    #print(json.dumps(json_object, indent = 1))
    #print(preInstalledResult[1])
    
    return JsonResponse({'status':'success'})



