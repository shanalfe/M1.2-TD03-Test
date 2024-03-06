from unittest.mock import Mock
from carte_pizzeria import CartePizzeria
from pizza import Pizza

class TestCartePizzaria():

    def test_nb_pizzas(self):
        pizza = Mock()
        carte_pizza = CartePizzeria()
        carte_pizza.pizzas = ["calzone", "4fromages", "mielChevre", "marocaine"]
        assert carte_pizza.nb_pizzas() == 4

    def test_carte_pizzaria_remove_pizza(self):
        pizza = Mock()
        carte_pizza = CartePizzeria()
        carte_pizza.pizzas = ["calzone", "4fromages"]
        carte_pizza.remove_pizza("4fromages")
        assert carte_pizza.nb_pizzas() == 1  
     
    def test_carte_pizzaria_add(self):
        carte = CartePizzeria()
        carte.pizzas = [Mock("1")]
        assert carte.nb_pizzas() == 1