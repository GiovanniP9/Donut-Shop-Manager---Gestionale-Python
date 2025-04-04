import re
#classe di test
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

import re  # Importa il modulo re per utilizzare le espressioni regolari

# Classe che gestisce l'autenticazione e la registrazione degli utenti
class Autenticator:
    def __init__(self, user_instance):
        # Salva l'istanza di User passata come parametro
        self.user_instance = user_instance
        
        # La regex per la validazione della password
        self.regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!?]).{8,}$"

    # Metodo per effettuare il login
    def login(self):
        # Richiede nome utente e password
        usName = input('Inserisci nome utente ---> ')
        usPass = input('Inserisci password ---> ')
        
        # Cerca l'utente nel dizionario 'users' per verificare se le credenziali sono corrette
        for key, val in self.user_instance.users.items():
            if val["username"] == usName and val["password"] == usPass:
                # Se trovata una corrispondenza, imposta la sessione dell'utente
                print(f'Login effettuato con successo, benvenuto {val["username"]}')
                self.user_instance.idSession = key  # Salva l'ID della sessione dell'utente
                return True
        
        # Se nessuna corrispondenza viene trovata
        print('Errore nel login...')
        return False
    
    # Metodo per registrare un nuovo utente
    def register(self):
        # Richiede il nome utente
        new_username = input('Scegli un nome utente ---> ')
        
        # Ciclo per chiedere una password finché non è valida
        while True:
            new_password = input('Scegli una password ---> ')
            
            # Controlla se la password rispetta i requisiti usando la regex
            if re.match(self.regex, new_password):
                break  # Esce dal ciclo se la password è valida
            else:
                # Mostra un messaggio di errore se la password non è valida
                print("Password non valida. Deve contenere almeno 8 caratteri, un numero, una maiuscola e un carattere speciale tra ! e ?.")
        
        # Calcola un nuovo ID per l'utente
        new_id = max(self.user_instance.users.keys()) + 1  # Prende il massimo ID e aggiunge 1
        
        # Aggiunge il nuovo utente al dizionario 'users'
        self.user_instance.users[new_id] = {'username': new_username, 'password': new_password}
        
        # Mostra un messaggio di conferma
        print(f'Utente {new_username} registrato con successo.')
        
    # Metodo per effettuare il logout
    def unLogin(self):
        # Imposta l'ID della sessione a -1 per disconnettere l'utente
        self.user_instance.idSession = -1
        # Stampa un messaggio di conferma
        print('Sei uscito')

      
user = User()
aut = Autenticator(user)
aut.login()
aut.register()