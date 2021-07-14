# Instrukcja instalacji dla systemu windows

- wymagane:
.python
.pip
.postgreSQL
.przeglądarka internetowa

1 Stwórz środowisko wirtualne

`python -m venv env`

2 Aktuwój środowisko wirtualne

'env\Script\activate`

3 Zainstaluj pakiety z pliku requirements.txt

`pip install -r requirements.txt`

4 Stwórz bazę danych postgresql oraz utwórz dla niej klienta, wraz ze wszystkimi uprawnieniami

5 W pliku settings.py w DATABASES uzupełnij nazwę strzorzonej bazy (NAME) oraz dane klienta (USER, PASSWORD)  

6 Wykonaj migrację

`python manage.py migrate`

7 Stwórz konto super użytkownika

`python manage.py createsuperuser`

8 Uruchom aplikajcję na localhost

`python manage.py runserver 8000`

9 W pole wyszukiwania przeglądarki internetowej wpisz : localhost:8000
