# Anleitung "Django Projekt lokal nutzen"

### Ordner erstellen, in dem das Projekt liegen soll.
_Ich habe dafür einfach einen Ordner auf meinem Desktop erstellt._

### Mit der Powershell in den erstellten Ordner navigieren.
_In meinem Fall:_
`cd Desktop/DjangoOrdner`

### Virtual Environment in diesen Ordner installieren.
`py -m venv venv`

_(das zweite "venv" ist einfach der Name der Umgebung. Die kann beliebig heißen.)_

### Dateien aus GitHub runterladen und im Ordner einfügen.
_Alle Dateien, die ich hochgeladen habe, entsprechen schon einem Projekt (se2network) und einer App (sociall)._

_Auf der Branch-Startseite auf den grünen '<>Code'-Button drücken, links auf 'local' navigieren und auf 'Download zip' klicken._

_die zip-datei in den erstellten DjangoOrdner entpacken. der Inhalt (Also die beiden Ordner und die drei Dateien) müssen auf der gleichen Ebene wie der venv-Ordner liegen._

### Django im Ordner installieren
`pip install django`

### Venv starten.
`.\venv\Scripts\activate`

### virtuellen Server starten
`py manage.py runserver`

### Projekt bzw. app im Browser öffnen
> 127.0.0.1:8000/

_Mit strg+c kann der Server wieder geschlossen werden._
