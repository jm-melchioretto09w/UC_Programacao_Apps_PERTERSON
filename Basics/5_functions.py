def helloWorld():
    print("Hello World!")
helloWorld()

def hello(name: str):
    print(f"Hello {name}")

name = "JM"
hello(name)
hello("Batata")

def ageCheck(name: str, age: int):
    print(f"Hello {name}, you are {age} years old, therefor, you are " + "an adult" if age > 18 else "a child")
ageCheck("Batata", 18)
ageCheck("JM", 17)