def sphere(R):
    Volume = (4/3)*(3.14 * R**3)
    return Volume
R = float(input("Radius: "))
aa= sphere(R)
print(f"the volume sphere equalent to {aa}")