class Symbol:
    def __init__(self, name):
        self.name = name

# Define class attributes after the class definition
Symbol.mustard = Symbol("ColMustard")
Symbol.plum = Symbol("ProfPlum")
Symbol.scarlet = Symbol("MsScarlet")
Symbol.characters = [Symbol.mustard, Symbol.plum, Symbol.scarlet]

Symbol.ballroom = Symbol("ballroom")
Symbol.kitchen = Symbol("kitchen")
Symbol.library = Symbol("library")
Symbol.rooms = [Symbol.ballroom, Symbol.kitchen, Symbol.library]

Symbol.knife = Symbol("knife")
Symbol.revolver = Symbol("revolver")
Symbol.wrench = Symbol("wrench")
Symbol.weapons = [Symbol.knife, Symbol.revolver, Symbol.wrench]

# Combine all symbols
Symbol.symbols = Symbol.characters + Symbol.rooms + Symbol.weapons

# Now you can create an instance of the Symbol class
symbols_instance = Symbol("example")

# Print the instance
print(symbols_instance)
