def ounces(grams):
    o = grams * 28.3495231
    return o

grams = float(input("grams: "))
aa = ounces(grams)
print(f"{grams} grams are equal to {aa} ounces")
