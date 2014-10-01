# PyCharmers Lesson 1

Welcome to week one of PyCharmers. To start, we'll be going over an introduction to Python, a general-purpose, high-level programming language. For those of you familiar with MATLAB, we'll try to draw parallels between the two languages throughout our introduction.

## Getting Started

Once Python is installed, we can start writing and evaluating some code by opening IDLE, the IDE (Integrated Development Environment) installed by default with Python.

When you launch IDLE, you'll probably see a prompt that looks something like this:

    Python 3.4.1 (default, Sep  9 2014, 11:21:41)
    [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.34.4)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

The `>>>` is the prompt, and code you write will appear after it. In examples, I'll omit the prompt, but you will always see it. This terminal is called a REPL, which stands for "read-evaluate-print-loop." When you press enter, the line you've entered is *read* by the interpreter, *evaluated*, and the result *printed* for you to see. Then the prompt displays again and the *loop* continues.

## Basic Syntax

Variables are declared in Python simply by introducing them:

    >>> x = 5
    >>> x
    5

The variable `x` now has the value `5`. Entering `x` in the REPL will now print its value.

### Operators

We can treat the REPL like a calculator. Enter math expressions and it will print the results:

#### Addition, subtraction, multiplication, and division

    >>> 6 + 6
    12
    >>> 6 - 12
    -6
    >>> 6 * -6
    -36
    >>> -36 / 6
    -6

#### Exponentiation

    >>> 6 ** 6
    46656

As shown above, we can raise numbers to powers using the `**` operator. We can also use parentheses to group more complex expressions.

    >>> (6 * 5 - (4 + 3)) ** 3
    12167

#### Assignment Operators

You can also combine operators with assignments for when you want to modify the value of a variable in place.

    >>> x = 5
    >>> x += 6
    >>> x
    11
    >>> x -= 4
    >>> x
    7
    >>> x *= -6
    >>> x
    -42
    >>> x /= 2
    >>> x
    -21

## Boolean Logic

Python also supports a number of boolean operators for evaluating conditions:

|Operator|Syntax|
|--------|:----:|
| Equal | `==` |
| Not Equal | `!=` |
| Greater than | `>` |
| Greater than or equal | `>=` |
| Less than | `<` |
| Less than or equal | `<=` |

The Python expressions `True` and `False` represent results of boolean expressions.

    >>> 4 == 4
    True
    >>> x = 5
    >>> y = 7
    >>> x == y
    False
    >>> x < y
    True

Note the difference between `=` and `==`. A single `=` is an assignment operator. So writing a comparison with one will (hopefully) cause the interpreter to fail:

    >>> 4 = 4
      File "<stdin>", line 1
    SyntaxError: can't assign to literal

More on errors later.

## Control Flow

Conditionals are great because we can use them to control what code gets executed in our programs.

#### If Statements

For example, we can inform the user if a variable is less than 5:

    if x < 5:
        print("x is less than 5")

**A quick syntactical note!** Python is a *whitespace-sensitive language*. That means that it matters how you indent your code. Code in the body of an if statement (or any statement followed by a colon, really) is indented one level further than the containing statement. So watch your indents!

In the above code, whatever goes in the parentheses will be printed to the console by `print`. We can add more branches to the behavior of this program with `elif` ("else if") and `else`:

    if x < 5:
        print("x is less than 5")
    elif x > 10:
        print("x is greater than 10")
    else:
        print("x is between 5 and 10 (inclusive)")

The code will only run once based on the value of `x`, so if the code in `else` gets run, we know that `x` must be between `5` and `10`. It's not good practice to have `if` or `elif` branches with overlapping conditions, but if your code does, only the first branch with a matching condition will run.

#### Loops

We can also use conditionals to run the same code multiple times. There are two main ways to do this.

##### For Loops

A for loop is useful to iterate through a set of data.

    for i in range(1, 11):
        print(i)

This code will print

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10

The function `range` will start with the first argument and go until the last argument (non-inclusive).

##### While Loops

While loops also run the same code multiple times, but they have different end conditions. While loops are better used when you don't know exactly how many times you want the loop to run, but you know when you want it to stop.

    i = 10
    while i > 0:
        print i
        i -= 1

This loop will print and decrement `i` on each iteration, producing this output:

    10
    9
    8
    7
    6
    5
    4
    3
    2
    1

## Strings

Now we'll begin to understand `print` a bit more from two angles, starting with strings. In Python, a "string literal" is enclosed by either `'` or `"` (single or double quotes). In programming, a "literal" refers to a value that is baked into the code -- that is, it is decided by the programmer before the program runs, and cannot be changed while the program is running.

    >>> string = "This is a string"
    >>> print(string)
    This is a string

We can do math with strings!

    >>> "a" + "a"
    'aa'
    >>> "a" * 5
    'aaaaa'
    >>> ("a" + ("b" + "c") * 3) * 5
    'abcbcbcabcbcbcabcbcbcabcbcbcabcbcbc'

Division, subtraction, and exponentiation are not defined. If you try them, you'll get an error.

## Error Messages

By now, you might have entered something incorrectly and seen one of Python's helpful error messages:

    >>> "a" ** 5
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

This is Python telling us that we can't raise a string to a power -- it knows what we are trying to do and tells us that this operation has not been defined.

If you haven't gotten any error messages yet, try entering some wrongs things. See if you can find out why Python reports the errors that it does.

In any real project with more than one line of code, Python will try its best to determine the line number of the error, but it won't always get it right. So it's always best to extend your search to before the line identified by the interpreter.

## Functions

Functions in Python are a lot like those in MATLAB.

    def printargs(arg1, arg2):
        print("arg1", "arg2")

This simple function just prints its arguments. The print function will print its arguments in order on the same line -- here we've given it two.

Most functions will perform some operation on their arguments and return the result for use somewhere else in the program.

    def multexp(in, mult, exp):
        result = (in * mult) ** exp
        return result

The return keyword ends execution of the function and returns the specified expression.

## Data Structures

Python has many useful data structures built in. For now we're just looking at lists, tuples, and briefly dictionaries. Different data structures represent data in ways that lend themselves best to different applications.

### Lists

Lists in Python are analogous to vectors in MATLAB. They are one-dimensional arrays of multiple values. There are many ways to create a list -- below is the shorthand:

    >>> alist = [2, 4, 6, 8]
    >>> alist
    [2, 4, 6, 8]

#### Indexing Lists

In Python, the first element of the list is element 0, not element 1 like MATLAB! There are many reasons why zero-indexing is preferable, but if you're used to one-indexing you'll just have to be careful at first.

    >>> alist[0]
    2
    >>> alist[3]
    8
    >>> alist[4]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

When we try to access an element outside the bounds of the array, Python warns us and ends execution. This is good behavior -- in lower-level languages like C, this would not happen. A C program using native C arrays would happily return whatever was in the memory right next to `alist[3]`. This behavior -- out-of-bounds array access -- was core to the critical [Heartbleed](http://heartbleed.com) bug in OpenSSL that swept the internet last Spring.

#### Updating Lists

We can change the values in a list simply by assigning to an indexed list, just like in MATLAB:

    >>> alist[2] = 9
    >>> alist
    [2, 4, 9, 8]

#### Indexing Strings

We can also index strings like lists because of how Python treats data types.

    >>> "a string"[4]
    'i'

### Tuples

Tuples are neat little constructs that open up a lot of interesting functionality. They're simple in concept and powerful in practice.

    >>> a = 5
    >>> b = 7
    >>> atuple = (a, b)
    >>> atuple
    (5, 7)

A tuple is basically a list of variables, but we can access their elements in more ways than we can those of a list.

Since we can implicitly define tuples on the left-hand side of an expression, we can use them to swap variables in one line:

    >>> a, b = b, a
    >>> a
    7
    >>> b
    5

This works because tuples are sensitive to order. Here the parentheses are not necessary, but the data structure that makes this possible is still the tuple.

Tuples also allow us to return multiple variables from a function:

    >>> def returntwo(a, b, c):
    ...     return b, c - a
    ...
    >>>
    >>> d, e = returntwo(3, 5, 7)
    >>> d
    5
    >>> e
    4

If we only provide one variable for this function to return to, it will be a tuple of the return values:

    >>> twovalues = returntwo(3, 5, 7)
    >>> twovalues
    (5, 4)

We can also access elements of tuples just like we do list elements:

    >>> twovalues[1]
    4

### Other Data Structures

Python has another extremely useful data structure: the dictionary. We didn't get to them this week at SLAC, but our example uses them! Basically, a dictionary in Python is like a list that is indexed with any kind of variable instead of a number. The variables we use to index are called "keys" and the variables they refer to are called "values", so a dictionary maps every key to exactly one value.

We can use dictionaries to map between names and ages, and index and modify them just like lists:

    >>> studentages = { "Evan D" : 20, "Ben K" : 20 }
    >>> studentages["Evan D"]
    20
    >>> studentages["Evan S"] = 22
    >>> studentages
    {'Evan D': 20, 'Ben K': 20, 'Evan S': 22}

## Example: Markov Chains

We used the above concepts to build the example, [markov.py](./markov/markov.py). It constructs a dictionary from a text file (the example uses William Shakespeare's Hamlet), and uses a [Markov chain](http://en.wikipedia.org/wiki/Markov_chain) to build new "sentences" in the style of the source text. We get results like this:

    A dull and muddy mettled rascal, peak, Like John a dreams, unpregnant of my father Queen.

    O heavy deed It had been so with us, We shall know by this hand.

    I lie in this case, should stir me most To my revenge.

A Markov chain, simply put, is a representation of connected states and the probabilities of transitioning between them. When we traverse a Markov chain, we jump from one state to the next based on the probability of each transition.

In this case, the states are groups of two words (prefixes) that appear consecutively in the text. Prefixes are connected if they themselves appear consecutively. So the Markov chain contains information about how sentences flow in the source text. New sentences are constructed by walking along the chain, making each transition at random, starting with a capital letter and ending with a period.

The example code is in `markov.py`. To run the code, `cd` to the folder in the command line and type `python markov.py`.

Take a look at the code and see if you can figure out what's going on. We'll go through the example in much more detail at SLAC next week.
