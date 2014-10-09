# PyCharmers Lesson 3
This week we are going to jump into some of the most powerful constructs in both Python and programming in general, objects! Objects aren't actually very complicated, but give us a ton of flexibility in how we organize our code and can be a really neat tool in how we think about problems. But perhaps more importantly, objects will help us make some graphical interfaces!

##Objects and Methods
In Python, every piece of data is what in computing we call an **object**. An object is something that can both have state, and act according to certain behaviors. Let's think about some of the objects we've used so far, and how they might fit this description.

To start off, consider the integer 3.

```py
>>> x = 3
>>> x
3
```

Here `x` is an `int` object, that holds the value 3 as its state. We expect `x` to behave in a certain way when we try to perform certain actions with it.

```py
>>> x += 1
>>> x
4
```

Same with lists.

```py
>>> myList = [1, 2, 3]
>>> myList
[1, 2, 3]
>>> myList[0] = 5
>>> myList
[5, 2, 3]
```

###Classes
We can also define our own type of object, with its own state, and its own behavior. We do this by defining a **class**, an outline for objects. Let's try creating a class to represent a dog, and start off by defining the state.

```py
>>> class Dog :
>>>   age = 3
>>>   name = "Spot"
>>> spot = Dog()
>>> spot
<__main__.Dog instance at 0x10636d878>
>>> spot.name
"Spot"
```

Here we've defined a Dog object that has a name and an age. We can define the behavior using what are called methods.

```py
>>> class Dog :
>>>   age = 3
>>>   name = "Spot"
>>>   def speak() :
>>>     print "ruff"
>>>   def nap() :
>>>     print "zzz"
>>> spot = Dog()
>>> spot.speak()
"ruff"
>>> spot.nap()
"zzz"
```

###Python Docs
You can see all of the documentation for Python standard classes and their methods on the [Python Docs website.](https://docs.python.org/3/)

##PyGame
To install PyGame, open a terminal and type
```sh
pip install pygame
```

If you get an error, try

```sh
sudo apt-get build-dep python-pygame
sudo apt-get install python-dev
```
