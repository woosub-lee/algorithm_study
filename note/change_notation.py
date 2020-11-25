def decimal2Nnotation(number, notation):
    result = []
    while(number >= notation):
        result.append(number % notation)
        number = number // notation
    result.append(number)
    result.reverse()
    print(result)
decimal2Nnotation(45,3)