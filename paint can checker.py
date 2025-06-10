# def greet():
#     print("Hello")
#     print("How are you?")
#     print("Bye")
#
# def greet_with(name, location):
#     print(f"Hello {name} and {location}")
#
# greet_with("Ariyan", "India")
# greet_with(location="India", name="Ariyan")
import math

def paint_calc(height, width, coverage):
    no_of_cans = math.ceil((int(height)*int(width))/coverage)
    print(f"you will need {no_of_cans} cans")
test_h = input("Height\n")
test_w = input("Width\n")
coverage = 5
paint_calc(height = test_h, width = test_w, coverage = coverage)