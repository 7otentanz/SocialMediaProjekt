import json
import os
#from django.contrib.auth.models import User -- gar nicht nötig obwohl wir auf den user zugreifen. Scheint aber zu klappen

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
    residence = "Engelsbrand" #hier irgendwie durch die Profileinstellungen den Wohnort setzen
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
    userpic = "Hier einen Pfad einfügen!" #hier irgendwie durch die Profileinstellungen das Profilbild setzen
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
            
