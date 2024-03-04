def count(a):
    try:
        with open(a, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return "file is unreal"
        

a = input("enter name of the file: ")
aa = count(a)
if aa=="file is unreal":
    print(aa)
else:
    print(f"count the number of lines in a text file: {count(a)}")