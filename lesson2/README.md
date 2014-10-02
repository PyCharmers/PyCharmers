#PyCharmers Lesson 2
Welcome to week 2 of PyCharmers! Hopefully by now you should have Ubuntu installed and are ready to start hacking around in your beautiful new Linux environment. This week we are going to briefly cover some useful command line tools and put them to use as we learn more about Python.

##Unix Tips and Tricks
Go ahead and open up your "Terminal" application, bonus points if you can figure out the hotkey to open it from anywhere.

##Functions
In the past, we've used functions like `print()` and `range()`, but today, we're going to write our own.

If you're unfamiliar, a function can be used to define a block of code that can be called over and over. This helps cut back on the amount of code you need to write if you have a certain task you want to carry out multiple times.

Let's start out with a simple function that just prints some text, and try calling it.

```py
>>> def myCoolFunction () :
>>>   print("This is such a cool function!")
>>> myCoolFunction()
"This is such a cool function!"
```

Awesome! Did you know we can also pass variables into a function? Let's try that.

```py
>>> def functionWithParams ( parameter1, parameter2 ) :
>>>   print(parameter1 + parameter2)
>>> functionWithParams(3, 2)
5
```

We can also write functions that return some data. When we do this, we can treat the function as if it were the returned data. For example

```py
>>> def multiplyByFive( i ) :
>>>   return i * 5
>>> x = multiplyByFive(3)
>>> x
15
```

Now that we've got the basics down, try creating a factorial function. After you create the function, you should be able to do something like this

```py
>>> factorial(5)
120
>>> factorial(10)
3628800
```

##Dictionaries
Last week we talked about a few [data structures](http://en.wikipedia.org/wiki/Data_structure) in Python, namely strings, lists, and tuples. This week, we're going to learn about another one of Python's data structures, the dictionary!

A dictionary in Python is a collection of labelled data. Let's try creating one.

```py
>>> myDictionary = {}
>>> myDictionary
{}
>>> otherDictionary = dict()
>>> otherDictionary
{}
```

Cool. We just created an empty dictionary, but that's pretty boring. Let's try creating a dictionary with some data, shall we?

```py
>>> myDictionary = {"bananas" : 4, "apples" : 2}
>>> myDictionary
{'bananas': 4, 'apples': 2}
```

Ahh, that's better. But wait, what did we just do? Dictionaries allow you to store any piece of data (strings, lists, even other dictionaries) and assign a label to it. In computing we call the label a **key** and the data a **value**. Here we've stored the value 4 with the key `"bananas"`, and 2 with the key `"apples"`.

We can get the data out of our dictionary similar to how we get data out of a list.

```py
>>> myList = [4, 0, 7]
>>> myList[2]
7
>>> myDictionary["bananas"]
4
```

You can also add or modify values after you've already created your dictionary.

```py
>>> myDictionary["oranges"] = "I like oranges"
>>> myDictionary
{'bananas': 4, 'apples': 2, 'oranges': "I like oranges"}
```
```py
>>> myDictionary["bananas"] = [3, 5, 7]
>>> myDictionary
{'bananas': [3, 5, 7], 'apples': 2, 'oranges': "I like oranges"}
```

You can even use tuples and numbers as keys!

```py
>>> myDict = {4 : "four", 3.14 : "pi", (1,2) : "onetwo"}
>>> myDict
{(1, 2): 'onetwo', 3.14: 'pi', 4: 'four'}
>>>
```

On your own try writing a function that takes as input two lists of matching length and return a dictionary in which the keys are the entries from the first list, and the values are the corresponding entries from the second list.

##Markov Review

Once you feel comfortable with the above material, go ahead and read through the markov.py [script](../lesson1/markov.py). Try to work through the comments to understand how the script is working. Then, make a local copy of the script and play around with it. Add some print statements to see what some of the datastructures look like. Try changing the loop behaviors to change the number of words in the dictionary key tuples. Try changing when a sentence should end. Can you make some awesome new sentences by modyfing the functionality?