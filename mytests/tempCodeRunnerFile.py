    people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    symbols = []


    for person in people:
        for house in houses:
            symbols.append(Symbol(f"{person}{house}"))
