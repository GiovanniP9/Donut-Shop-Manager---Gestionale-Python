class User:
    def __init__(self, username, password):
        self.username = username  # Inizializza l'oggetto User con un username e una password forniti al momento della creazione
        self.password = password

        # Dizionario con utenti
        # id univoco dell'utente,
        # mentre il valore è un dizionario con le chiavi 'username' e 'password'.
        self.users = {
            1: {'username': 'Homer', 'password': 'fozzanapoli123'},
            2: {'username': 'pippo_da_crotone', 'password': 'vengodavibovalentia'},
            3: {'username': 'lol', 'password': 'makekazz'}
        }
        
        self.idSession = -1 # Il valore -1 indica che nessun utente ha effettuato il login.

    def update_data(self):
        # Verifica se l'utente ha effettuato il login.
        if self.idSession == -1:
            print('Effettua il login prima di modificare i dati.')
            return  # Interrompe l'esecuzione del metodo se non c'è un utente loggato

        print(self.users[self.idSession])
        
        nuovo_username = input("Inserisci il nuovo username: ")
        nuova_password = input("Inserisci la nuova password: ")

        if nuovo_username:
            self.users[self.idSession]['username'] = nuovo_username
            self.username = nuovo_username
        
        # Analogamente, se è stata inserita una nuova password, essa viene aggiornata nel dizionario
        # e nell'attributo self.password.
        if nuova_password:
            self.users[self.idSession]['password'] = nuova_password
            self.password = nuova_password

        # Messaggio di conferma per indicare che i dati sono stati aggiornati con successo.
        print("Dati aggiornati con successo!")
        # Stampa i nuovi dati dell'utente loggato, prelevandoli dal dizionario self.users.
        print("Nuovi dati:", self.users[self.idSession])
