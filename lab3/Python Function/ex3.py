def solve(numheads, numlegs):
    y = int((numlegs - 2*numheads)/2)
    return y

numheads, numlegs = map(int, input("numheads, numlegs : ").split(" "))
rabbits = solve(numheads, numlegs)
print(f"in ferm we have {rabbits} rabbits and {numheads - rabbits} chikens")

