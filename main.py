import re
import logging

# Configurazione di base per il logging
logging.basicConfig(level=logging.INFO)

# Decoratore per tracciare la chiamata di una funzione
def is_called(func):
    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__} is called")
        res = func(*args, **kwargs)
        logging.info(f"{func.__name__} is executed with args:{args} and kwargs:{kwargs}")
        return res
    return wrapper

# Classe User: gestisce le informazioni e i dati degli utenti
class User:
    def __init__(self, username, password):
        # Inizializza l'oggetto User con username e password forniti
        self.username = username  
        self.password = password

        # Dizionario con utenti predefiniti: la chiave è l'ID univoco,
        # il valore è un dizionario contenente 'username' e 'password'.
        self.users = {
            1: {'username': 'Homer', 'password': 'fozzanapoli123'},
            2: {'username': 'pippo_da_crotone', 'password': 'vengodavibovalentia'},
            3: {'username': 'lol', 'password': 'makekazz'}
        }
        
        # idSession: -1 indica che nessun utente ha effettuato il login.
        self.idSession = -1

    @is_called
    def update_data(self):
        # Verifica se l'utente ha effettuato il login
        if self.idSession == -1:
            print('Effettua il login prima di modificare i dati.')
            return

        # Mostra i dati attuali dell'utente loggato
        print("Dati attuali:", self.users[self.idSession])
        
        # Richiede all'utente i nuovi dati
        nuovo_username = input("Inserisci il nuovo username: ")
        nuova_password = input("Inserisci la nuova password: ")

        # Se l'utente inserisce un nuovo username, aggiorna i dati
        if nuovo_username:
            self.users[self.idSession]['username'] = nuovo_username
            self.username = nuovo_username
        
        # Se l'utente inserisce una nuova password, aggiorna i dati
        if nuova_password:
            self.users[self.idSession]['password'] = nuova_password
            self.password = nuova_password

        # Conferma l'aggiornamento e mostra i nuovi dati
        print("Dati aggiornati con successo!")
        print("Nuovi dati:", self.users[self.idSession])

# Classe Autenticator: gestisce login e registrazione
class Autenticator:
    def __init__(self, user_instance):
        # Salva l'istanza di User passata come parametro
        self.user_instance = user_instance
        # Regex per validare la password:
        # deve contenere almeno 8 caratteri, almeno una maiuscola, un numero e un carattere speciale tra ! e ?
        self.regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!?]).{8,}$"

    @is_called
    def login(self):
        # Richiede nome utente e password
        usName = input('Inserisci nome utente ---> ')
        usPass = input('Inserisci password ---> ')
        
        # Verifica le credenziali cercando nel dizionario degli utenti
        for key, val in self.user_instance.users.items():
            if val["username"] == usName and val["password"] == usPass:
                print(f'Login effettuato con successo, benvenuto {val["username"]}')
                self.user_instance.idSession = key  # Salva l'ID della sessione
                return True
        
        print('Errore nel login...')
        return False

    @is_called
    def register(self):
        # Richiede il nome utente per la registrazione
        new_username = input('Scegli un nome utente ---> ')
        
        # Chiede la password finché non rispetta i requisiti della regex
        while True:
            new_password = input('Scegli una password ---> ')
            if re.match(self.regex, new_password):
                break
            else:
                print("Password non valida. Deve contenere almeno 8 caratteri, un numero, una maiuscola e un carattere speciale tra ! e ?.")
        
        # Calcola un nuovo ID basandosi sul massimo attuale
        new_id = max(self.user_instance.users.keys()) + 1
        self.user_instance.users[new_id] = {'username': new_username, 'password': new_password}
        
        print(f'Utente {new_username} registrato con successo.')
        
    @is_called
    def unLogin(self):
        # Effettua il logout impostando idSession a -1
        self.user_instance.idSession = -1
        print('Sei uscito')

# Classe Donut: rappresenta un donut con il relativo prezzo e costo di produzione
class Donut:
    """Donut represents a real donut you can buy in a store"""
    def __init__(self, name: str, sale_price: float, production_cost: float) -> None:
        self.name = name
        self.price = sale_price
        self.prod_cost = production_cost
        
    @is_called    
    def calculate_profit(self):
        # Calcola il profitto come differenza tra prezzo di vendita e costo di produzione
        return self.price - self.prod_cost

# Classe store: gestisce l'inventario dei prodotti e il profitto totale
class store:
    def __init__(self):
        # Inizializza l'inventario e il profitto totale
        self.inventory = {}  # Le chiavi saranno oggetti prodotto (es. Donut)
        self.total_profit = 0
    
    def add_product(self, product, quantity):
        # Aggiunge un prodotto all'inventario o aggiorna la quantità esistente
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity
        print(f"Added {quantity} of {product.name} to inventory.")
        
    def sell_product(self, product_name, quantity):
        # Cerca il prodotto in inventario in base al nome
        found_product = None
        for product in self.inventory:
            if product.name == product_name:
                found_product = product
                break
        # Se il prodotto esiste e c'è quantità sufficiente, procede alla vendita
        if found_product is not None and self.inventory[found_product] >= quantity:
            self.inventory[found_product] -= quantity
            profit = found_product.calculate_profit() * quantity
            self.total_profit += profit
            print(f"Sold {quantity} of {found_product.name}. Profit: {profit}.")
        else:
            print("Product not available or insufficient quantity.") 
    
    def show_inventory(self):
        # Visualizza i prodotti in inventario
        print("Inventory:")
        if self.inventory:
            for product, quantity in self.inventory.items():
                print(f"{product.name}: {quantity} units")
        else:
            print("Inventory is empty.")
    
    def show_profit(self):
        # Mostra il profitto totale
        print(f"Total profit: {self.total_profit}")

# Funzione main per far interagire tutte le componenti
def main():
    # Creazione dell'istanza utente e del sistema di autenticazione
    user = User(username="", password="")
    auth = Autenticator(user)
    
    # Scelta tra login e registrazione
    choice = input("Vuoi fare login (l) o registrarti (r)? ")
    if choice.lower() == 'l':
        if not auth.login():
            return  # Termina se il login fallisce
    elif choice.lower() == 'r':
        auth.register()
    else:
        print("Scelta non valida.")
        return
    
    # Possibilità di aggiornare i dati dell'utente loggato
    update_choice = input("Vuoi aggiornare i tuoi dati? (s/n) ")
    if update_choice.lower() == 's':
        user.update_data()
    
    # Creazione dello store e aggiunta di alcuni prodotti
    my_store = store()
    donut1 = Donut("Glazed", 1.5, 0.5)
    donut2 = Donut("Chocolate", 2.0, 0.8)
    my_store.add_product(donut1, 10)
    my_store.add_product(donut2, 5)
    
    # Ciclo di menu interattivo
    while True:
        print("\n=== Menu Principale ===")
        print("1. Visualizza inventario")
        print("2. Vendi prodotto")
        print("3. Visualizza profitto")
        print("4. Aggiorna dati utente")
        print("5. Esci")
        
        option = input("Scegli un'opzione: ")
        
        match option:
            case "1":
                my_store.show_inventory()
            case "2":
                sell_choice = input("Inserisci il nome del donut da vendere: ")
                try:
                    quantity = int(input("Inserisci la quantità da vendere: "))
                except ValueError:
                    print("Quantità non valida.")
                    continue
                my_store.sell_product(sell_choice, quantity)
            case "3":
                my_store.show_profit()
            case "4":
                user.update_data()
            case "5":
                print("Uscita dal programma. Alla prossima!")
                break
            case _:
                print("Opzione non valida, riprova.")


main()
