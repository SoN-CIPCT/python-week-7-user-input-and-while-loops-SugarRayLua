pizza_orders = ["pepperoni","anchovy","Hawaiian"]
finished_pizzas = []
while pizza_orders != []:
    for pizza in pizza_orders:
        print("Your "+pizza+" pizza pie is finished!")
        finished_pizzas.insert(0,pizza_orders.pop())
for pizza in finished_pizzas:
    print("The pizza "+pizza+" was made.")
