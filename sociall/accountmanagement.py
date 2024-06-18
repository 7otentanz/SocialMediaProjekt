import json
import os

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

def setresidence(request):
    residence = {"residence": "Engelsbrand"} #hier irgendwie durch die Profileinstellungen den Wohnort setzen
    user = request.user.username
    try:
        with open(f"./sociall/Accountmanagement/{user}.json", "a") as masterlist:
            residencedump = json.dumps(residence)
            masterlist.write(residencedump)
    except:
        print("Wohnort setzen hat nicht funktioniert!")
