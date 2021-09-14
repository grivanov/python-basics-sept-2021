checked = input()
fruit = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetable = ["tomato", "cucumber", "pepper", "carrot"]

if checked in fruit:
    print("fruit")
elif checked in vegetable:
    print("vegetable")
else:
    print("unknown")