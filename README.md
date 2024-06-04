# Anleitung "Django Projekt lokal nutzen"

### Ordner erstellen, in dem das Projekt liegen soll.
Ich habe dafür einfach einen Ordner auf meinem Desktop erstellt.

### Mit der Powershell in den erstellten Ordner navigieren.
In meinem Fall: 
> cd Desktop/DjangoOrdner

### Virtual Environment in diesen Ordner installieren.
> py -m venv venv

(das zweite "venv" ist einfach der Name der Umgebung. Die kann beliebig heißen.)

### Dateien aus GitHub runterladen und im Ordner einfügen.
Alle Dateien, die ich hochgeladen habe, entsprechen schon einem Projekt (se2network) und einer App (sociall).
Auf der Branch-Startseite auf den grünen '<>Code'-Button drücken, links auf 'local' navigieren und auf 'Download zip' klicken.
die zip-datei in den erstellten DjangoOrdner entpacken. der Inhalt (Also die beiden Ordner und die beiden Dateien) müssen auf der gleichen Ebene wie der venv-Ordner liegen.

### Venv starten.
> .\venv\Scripts\activate

### In den Projektordner navigieren.
> cd se2network

### virtuellen Server starten
> py manage.py runserver

### Projekt bzw. app im Browser öffnen
url: 127.0.0.1:8000/
