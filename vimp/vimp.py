import requests
from bs4 import BeautifulSoup

url_login = 'https://elearning.uni-regensburg.de/login/index.php'
url_startseite = 'https://elearning.uni-regensburg.de'
url_meine_Kurse ='https://elearning.uni-regensburg.de/my/'

anmeldedaten_korrekt = {
            'username' : 'lup42010',
            'password' : 'EUp!l38!',
            'realm' : 'hs',
          }

anmeldedaten_fehlerhaft ={
    'username': 'dsfa',
    'password':'safd',
    'realm':'gfds'
    }

with requests.Session() as session:
    #anmeldng im Elearning und erstellen des Objektes login
    print('Anmeldung wird durchgeführt...')
    login = session.post(url_login, data=anmeldedaten_korrekt)
    login.text
    after_login = BeautifulSoup(login.text, 'html.parser')
    titel = after_login.title

    anmeldung_erfolgreich= '<title>GRIPS - Uni Regensburg</title>'

    if titel is anmeldung_erfolgreich
        print('anmeldung erfolgreich')
    else:
        print('anmeldung fehlgeschlagen')


    #print('Anmeldung2 wird durchgeführt...')
    #login_2 = session.post(url_login, data=anmeldedaten_fehlerhaft)
    #login_2.text
    #after_login_2 = BeautifulSoup(login_2.text, 'html.parser')
    #titel_2 = after_login_2.title
    #print(titel)
    #print(titel_2)

    ##laden der Startseite in Ojekt
    #seite = session.get(url_meine_Kurse)
    #seite.text
    #soup = BeautifulSoup(seite.text, 'html.parser')


    #soup.find_all('html_elemen', class_='qa-blocklist unlist')


    print('fertig')
