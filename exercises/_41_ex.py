###~~~Learning to Speak Object-Oriented~~~###
###~~~oop_test.py is the script for this exercise###

~Word Drills~
class           Tell Python to make a new type of thing
object          Two meanings: the most basic type of thing, and any instance of some thing
instance        What you get when you tell Python to create a class
def             How you define a function inside a class
self            Inside the functions in a class, self is a variable for the instance/object being accessed
inheritance     The concept that one class can inherit traits from another class
composition     The concept that a class can be composed of other classes as parts, much like how a car has wheels
attribute       A property classes have that are from compoosition and are usually variables
is-a            A phrase to say that something inherits from another, as in a "salmon" is-a "fish"
has-a           A phrase to say that something is comoposed of other things or has a trait, as in a "salmon" has-a "mouth"


~Phrase Drills~
class X(y)                      Make a class named X that is-a Y
class X(object):                Class X has-a __init__ that takes self and J parameters
    def __init__(self, J)
class X(object):                Class X has-a function named M that takes self and J parameters
    def M(self, J)
foo = X()                       Set foo to an instance of class X
foo.M(J)                        From foo, get the M function, and call it with parameters self, J
foo.K = Q                       From foo, get the K attribute, and set it to Q