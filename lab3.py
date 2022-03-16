def slength1(s):
    if len(s) > 10:
        ans = "very long"
    else:
        ans = "normal"

    return ans

print(slength1("Hello"))


def f(x):
    return x**2, x**3

a, b = f(2)

print(f(2))

a = "Hello swiat"

a = a[0:3] + "x" +  a[4:]

print(a)

print(list(range(5)))
animals = ['dog', 'cat', 'mouse']
for animal in animals:
    print("This is the {}".format(animal))

for i in range(101):
    print("Kwadrat {} to {}".format(i, i**2))

for letter in "Hello World":
    print(letter)

