import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

    os.rename(f"{user}.json", f"./sociall/Accountmanagement/{user}.json")


#Fügt der bestehenden Nutzer.json den Wohnort in das bestehende Dictionary hinzu
def setresidence(request):
    residence = save_string(request)
    user = request.user.username
    with open(f"./sociall/Accountmanagement/{user}.json", "r") as masterlist:
        accountdict = json.loads(masterlist.read())
        accountdict["residence"] = residence

    try:
        with open(f"./sociall/Accountmanagement/{user}.json", "w") as masterlist:
            accountdictdump = json.dumps(accountdict)
            masterlist.write(accountdictdump)
    except:
        print("Wohnort setzen hat nicht funktioniert!")


#Fügt der bestehenden Nutzer.json das Profilbild in das bestehende Dictionary hinzu
def setuserpic(request):
    userpic = save_string(request)
    user = request.user.username
    with open(f"./sociall/Accountmanagement/{user}.json", "r") as masterlist:
        accountdict = json.loads(masterlist.read())
        accountdict["userpic"] = userpic

    try:
        with open(f"./sociall/Accountmanagement/{user}.json", "w") as masterlist:
            accountdictdump = json.dumps(accountdict)
            masterlist.write(accountdictdump)
    except:
        print("Nutzerbild setzen hat nicht funktioniert!")

