

# print('How many pizzas do you want to order?')
# quantity = input()

# while quantity != input:
#     toppings = int(input('How many toppings for pizza {} \n'))
#     toppings2 = int(input('you have ordered a pizza with {} toppings\n'.format(toppings)))
        
#     break
quantity = int(input('How many pizzas do you want to order?'))
inputs = []
for x in range(quantity):
    inputs.append(input('How many toppings for pizza {} \n'.format(quantity)))
        
