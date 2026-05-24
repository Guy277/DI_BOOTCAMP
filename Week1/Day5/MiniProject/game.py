import random

class Game:
    
    def get_user_item(self):
        # Boucle jusqu'à ce que l'utilisateur fasse un choix valide
        while True:
            user_input = input("Select (r)ock, (p)aper, or (s)cissors: ").lower()
            if user_input in ["r", "p", "s"]:
                return user_input  # On retourne le choix valide
            else:
                print("Invalid choice. Please choose r, p, or s.")

    def get_computer_item(self):
        # L'ordinateur choisit aléatoirement parmi r, p, s
        return random.choice(["r", "p", "s"])

    def get_game_result(self, user_item, computer_item):
        # Match nul si les deux choix sont identiques
        if user_item == computer_item:
            return "draw"
        
        # Cas où l'utilisateur gagne
        elif (user_item == "r" and computer_item == "s") or \
             (user_item == "p" and computer_item == "r") or \
             (user_item == "s" and computer_item == "p"):
            return "win"
        
        # Sinon l'utilisateur perd
        else:
            return "loss"

    def play(self):
        # Récupère le choix de l'utilisateur
        user_item = self.get_user_item()
        
        # Récupère le choix de l'ordinateur
        computer_item = self.get_computer_item()
        
        # Détermine le résultat
        result = self.get_game_result(user_item, computer_item)
        
        # Affiche le résultat
        print(f"You chose: {user_item}. The computer chose: {computer_item}. Result: {result}")
        
        # Retourne le résultat (win / loss / draw)
        return result