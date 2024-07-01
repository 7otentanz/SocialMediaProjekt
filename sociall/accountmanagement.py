import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from geopy.geocoders import Nominatim

# Daten aus dem localStorage empfangen
@csrf_exempt
def save_string(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        stored_string = data.get('storedString', '')
        return stored_string
    print("Nö. das ging schief.")

#Erstellt die Nutzer.json mit dem ersten Inhalt: dem Nutzernamen.
def createprofile(request):
    user = request.user.username #user und username sind definiert in der django.contrib.auth.models - deshalb kann hier direkt auf den Namen zugegriffen werden!
    try:
        with open(f"{user}.json", "w") as masterlist:
              usernumber = {"username": f"{user}"}
              usernumberdump = json.dumps(usernumber)
              masterlist.write(usernumberdump)
    except:
          print("Nutzer.json anlegen hat nicht funktioniert!")

    os.rename(f"{user}.json", f"./sociall/static/Accountmanagement/{user}.json")


#Fügt der bestehenden Nutzer.json den Wohnort in das bestehende Dictionary hinzu
def setresidence(request):
    residence = save_string(request)

    #geopy um den Wohnort in Koordination zu übersetzen
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(residence)

    user = request.user.username
    try:
        with open(f"./sociall/static/Accountmanagement/{user}.json", "r") as masterlist:
            accountdict = json.loads(masterlist.read())
            accountdict["residence"] = [location.longitude, location.latitude]
    except:
        print("Kein Wohnort gesetzt!")

    try:
        with open(f"./sociall/static/Accountmanagement/{user}.json", "w") as masterlist:
            accountdictdump = json.dumps(accountdict)
            masterlist.write(accountdictdump)
    except:
        print("Wohnort setzen hat nicht funktioniert!")

#Holt den Wohnort aus der Nutzer.json heraus um sie einzufügen
def getresidence(request):
    user = request.user.username
    try:
        with open(f"./sociall/static/Accountmanagement/{user}.json", "r") as masterlist:
            accountdict = json.loads(masterlist.read())
            residence = accountdict["residence"]
            return residence
    except:
        print("Kein Wohnort gesetzt!")

#Fügt der bestehenden Nutzer.json das Profilbild in das bestehende Dictionary hinzu
def setuserpic(request):
    userpic = save_string(request)
    user = request.user.username
    with open(f"./sociall/static/Accountmanagement/{user}.json", "r") as masterlist:
        accountdict = json.loads(masterlist.read())
        accountdict["userpic"] = userpic

    try:
        with open(f"./sociall/static/Accountmanagement/{user}.json", "w") as masterlist:
            accountdictdump = json.dumps(accountdict)
            masterlist.write(accountdictdump)
    except:
        print("Nutzerbild setzen hat nicht funktioniert!")

#Holt das Profilbild aus der Nutzer.json um sie einzufügen
def getuserpic(request):
    user = request.user.username
    try:
        with open(f"./sociall/static/Accountmanagement/{user}.json", "r") as masterlist:
            accountdict = json.loads(masterlist.read())
            userpic = accountdict["userpic"]
            return userpic
    except:
        print("Kein Profilbild gesetzt!")
