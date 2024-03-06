
class CartePizzeria():
    def __init__(self):
        self.pizzas = []

    def is_empty(self):
        if len(self.pizzas):
            return False
        
    def nb_pizzas(self):
        return len(self.pizzas)
    
    def remove_pizza(self, nom_pizza):
        try:
            self.pizzas.remove(nom_pizza)
        #exception si la pizza n'existe pas
        except ValueError:
            raise CartePizzeriaException("Pas de pizza de ce nom")
         
class CartePizzeriaException(Exception):
    print("Erreur dans la carte de la pizzeria")