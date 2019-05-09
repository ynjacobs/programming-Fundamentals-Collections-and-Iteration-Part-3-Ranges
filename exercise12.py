

# print('How many pizzas do you want to order?')
# quantity = input()

# while quantity != input:
#     toppings = int(input('How many toppings for pizza {} \n'))
#     toppings2 = int(input('you have ordered a pizza with {} toppings\n'.format(toppings)))
        
#     break
pizza_id = 0
quantity = int(input('How many pizzas do you want to order?\n'))
toppings = {}
for x in range(quantity):
    pizza_id += 1
    topping = input('How many toppings for pizza {} \n'.format(pizza_id))
    toppings[pizza_id] = topping 
    print('you have ordered a pizza with {} toppings.'.format(topping))
        
