import requests
from bs4 import BeautifulSoup

url_login = 'https://elearning.uni-regensburg.de/login/index.php'
url_startseite = 'https://elearning.uni-regensburg.de'
url_meine_Kurse = 'https://elearning.uni-regensburg.de/my/'

anmeldedaten_korrekt = {
            'username' : 'lup42010',
            'password' : 'EUp!l38!',
            'realm' : 'hs',
          }

def check(str_to_compare, str_to_compare_to):
   if str_to_compare == str_to_compare_to:
      print("anmeldung erfolgreich")
      return True
   else:
      print("anmeldung fehlgeschlagen")
      return False

def get_login_data():

    anmeldedaten.benutzername = input('Benutername: ')
    anmeldedaten.passwort = input('Passwort: ')


with requests.Session() as session:
    #anmeldng im Elearning und erstellen des Objektes login
    print('Anmeldung wird durchgeführt...')
    login = session.post(url_login, anmeldedaten_korrekt)
    login.text
    after_login = BeautifulSoup(login.text, 'html.parser')
    titel = after_login.title.text

    #anmeldung_erfolgreich = "GRIPS - Uni Regensburg"

    #check(titel, anmeldung_erfolgreich)

    #laden der Startseite in Ojekt

    seite = session.get(url_meine_Kurse)
    seite.text
    soup = BeautifulSoup(seite.text, 'html.parser')

    hyperlinks = []

    for links in soup.find_all('a'):
        #print(soup.find_all('a'),list)
        hyperlinks.append(links.get('href'))

    #kürzen der Liste der Links
    kursliste = hyperlinks[hyperlinks.index('#sb-9')+1:hyperlinks.index('#sb-4')+1]


    print('fertig')


