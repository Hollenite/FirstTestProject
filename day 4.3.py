from webbrowser import Elinks

line1 = ["A1", "B1", "C1"]
line2 = ["A2", "B2", "C2"]
line3 = ["A3", "B3", "C3"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()

if position == "A1":
    line1 = ["x", "B1", "C1"]
elif position == "A2":
    line2 = ["x", "B2", "C2"]
elif position == "A3":
    line3 = ["x", "B3", "C3"]
elif position == "B1":
     line1 = ["A1", "x", "C1"]
elif position == "B2":
    line2 = ["A2", "x", "C2"]
elif position == "B3":
    line3 = ["A3", "x", "C3"]
elif position == "C1":
    line1 = ["A1", "B1", "X"]
elif position == "C2":
    line2 = ["A2", "B2", "X"]
elif position == "C3":
    line3 = ["A3", "B3", "X"]

print(f"{line1}\n{line2}\n{line3}")