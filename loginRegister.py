import re
class User:
  
  def __init__(self, name=None, password=None):
    self.name = name
    self.password = password
    self.users = {
        1: {'username': 'ciro', 'password': 'password123'},
        2: {'username': 'anna', 'password': 'securepass'},
        3: {'username': 'marco', 'password': '123456'}
    }
    self.idSession = -1
    
class Autenticator:
    def __init__(self, user_instance):
        self.user_instance = user_instance
        self.regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!?]).{8,}$"

    
    def login(self):
        usName = input('Inserisci nome utente ---> ')
        usPass = input('Inserisci password ---> ')
        for key, val in self.user_instance.users.items():
            if val["username"] == usName and val["password"] == usPass:
                print(f'Login effettuato con successo, benvenuto {val["username"]}')
                self.user_instance.idSession = key
                return True
        print('Errore nel login...')
        return False
    
    def register(self):
        new_username = input('Scegli un nome utente ---> ')
        while True:
          new_password = input('Scegli una password ---> ')
          if re.match(self.regex):
            break
          else:
            print("Password non valida. Deve contenere almeno 8 caratteri, un numero, una maiuscola e un carattere speciale tra ! e ?.")
        
        new_id = max(self.user_instance.users.keys()) + 1
        self.user_instance.users[new_id] = {'username': new_username, 'password': new_password}
        print(f'Utente {new_username} registrato con successo.')
        
    def unLogin(self):
      self.user_instance.idSession = -1
      print('Sei uscito')
      
user = User()
aut = Autenticator(user)
aut.login()
aut.register()