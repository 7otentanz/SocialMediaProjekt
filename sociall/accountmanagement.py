from django.contrib.auth.models import User
import json

def createprofile():
    all_users = User.objects.all()
    for item in all_users:
        try:
            with open(f"{item.username}.json", "w") as masterlist: #username ist definiert in der django.contrib.auth.models - deshalb kann hier direkt auf den Namen zugegriffen werden!
                usernumber = {"username": f"{item.username}"}
                usernumberdump = json.dumps(usernumber)
                masterlist.write(usernumberdump)
        except:
            with open(f"{item.username}.json", "r") as masterlist:
                masterlist.readline()
                return None

def setresidence(): #GEHT NOCH NICHT!!!! Und das oben sollte dann nicht mehr für alle gemacht werden...
    residence = {"residence": "Engelsbrand"} #hier irgendwie durch die Profileinstellungen den Wohnort setzen
    usernumber = str(User)
    try:
        with open(f"{usernumber}.json", "w") as masterlist:
            residencedump = json.dumps(residence)
            masterlist.write(residencedump)
    except:
        return None
            
