class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.users = {
            1: {'username':'Homer', 'password':'fozzanapoli123'},
            2: {'username':'pippo_da_crotone', 'password':'vengodavibovalentia'},
            3: {'username':'lol', 'password':'makekazz'}
        }
        
        self.idSession = -1
        

    def update_data(self):
        if self.idSession != -1:
            print('Effettua il login prima di modificare i dati.')
            return

        print(self.users[self.idSession])
        nuovo_username = input("Inserisci il nuovo username (premi invio per mantenere quello attuale): ")
        nuova_password = input("Inserisci la nuova password (premi invio per mantenere quella attuale): ")

        if nuovo_username:
            self.users[self.idSession]['username'] = nuovo_username
            self.username = nuovo_username
        if nuova_password:
            self.users[self.idSession]['password'] = nuova_password
            self.password = nuova_password

        print("Dati aggiornati con successo!")
        print("Nuovi dati:", self.users[self.idSession])
        
        
        