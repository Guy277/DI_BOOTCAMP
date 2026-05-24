from game import Game

def get_user_menu_choice():
    # Affiche le menu et retourne le choix de l'utilisateur
    print("\n    Menu:")
    print("    (g) Play a new game")
    print("    (x) Show scores and exit")
    choice = input("     : ").lower()
    return choice

def print_results(results):
    # Affiche le récapitulatif des parties
    print("\n    Game Results:")
    print(f"      You won {results['win']} times")
    print(f"      You lost {results['loss']} times")
    print(f"      You drew {results['draw']} times")
    print("\n    Thank you for playing!")

def main():
    # Dictionnaire pour stocker les résultats
    results = {"win": 0, "loss": 0, "draw": 0}
    
    # Boucle principale du menu
    while True:
        choice = get_user_menu_choice()
        
        if choice == "g":
            # Crée un nouvel objet Game et joue une partie
            game = Game()
            result = game.play()
            
            # Met à jour le compteur de résultats
            results[result] += 1
        
        elif choice == "x":
            # Affiche le résumé et quitte
            print_results(results)
            break
        
        else:
            print("Invalid choice. Please choose g or x.")

# Lance le programme
main()