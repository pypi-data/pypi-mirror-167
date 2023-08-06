from HectareaPES import PaneraPizza


#Plain Text
PizzaDough = b"How Big Are Panera's Flatbread Pizzas? Panera's pizzas are square-shaped and they're the perfect size for a personal pizza. They're about 11-inches long by 4-inches wide, and they're usually cut into 6 small squares, which makes it easy for portioning."


#Initial Value
Ingredients = b'Pepperoni Initial Value'


#Password
Sauce = b'Random Password'



PizzaBoxes = []

for PizzaBox in range(len(PizzaDough)//32):
    PizzaBoxes.append(PizzaDough[PizzaBox*32:PizzaBox*32+32])
PizzaBoxes.append(PizzaDough[len(PizzaDough)//32*32:len(PizzaDough)])


PizzaStack = b''

for Pizza in PizzaBoxes:

    RolledDough = PaneraPizza.RollingPin(Pizza, Sauce, Ingredients)


    SeasonedPizza = PaneraPizza.Mix(RolledDough, Sauce)


    FrozenPizza = PaneraPizza.Freezer(SeasonedPizza, Sauce)


    PizzaStack += FrozenPizza


    Sauce = Pizza


print(PizzaStack)
print(PizzaBoxes)





ReadyPizzas = b''


FrozenPizzaStack = []

for PizzaBox in range(len(PizzaStack)//32):
    FrozenPizzaStack.append(bytearray(PizzaStack[PizzaBox*32:PizzaBox*32+32]))
FrozenPizzaStack.append(bytearray(PizzaStack[len(PizzaStack)//32*32:len(PizzaStack)]))


Sauce=b'Random Password'


for FrozenPizza in FrozenPizzaStack:


    BakedPizza = PaneraPizza.Oven(FrozenPizza, Sauce)


    PizzaSlices = PaneraPizza.Cutter(BakedPizza, Sauce)


    PizzaSlice = PaneraPizza.Turner(PizzaSlices, Sauce, Ingredients)


    ReadyPizzas += PizzaSlice


    Sauce = PizzaSlice


print(ReadyPizzas)

