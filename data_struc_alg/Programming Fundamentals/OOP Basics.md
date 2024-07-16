Object-oriented programming is a type of programming that uses class instanced objects to design applications and software.

- Classes -
	Essential to OOP. You can create many instances of a class. Within these classes you can create methods to do work on individual instances of the class. Since you can create an instance of a class(object) when initialized it will always require the self argument that passes the object. Any methods defined in the class also require self as the first argument. Example of a class that utilizes properties and a method:

```
class Wall:
    def __init__(self, armor, magic_resistance):
        self.__armor = armor
        self.__magic_resistance = magic_resistance

    def get_defense(self):
        return self.__armor + self.__magic_resistance
```

Two kinds of variables in relation to classes. Class variables and instanced variables. Much like with global variables, it is best practice to avoid utilizing class variables over instanced ones.

- Encapsulation - 
	The most basic example of encapsulation is a function. The caller of a function doesn't need to worry too much about what happens inside, they just need to understand the inputs and outputs.

- Abstraction - 
	Abstraction is about creating a simple interface for complex behavior. An example would be libraries in python. they ABSTRACT the very complex work to just a simple import (think of the random libary). random.randrange() has its complexity encapsulated in the randrange function. Usually Abstraction and Encapsulation occur hand in hand. abstraction and encapsulation are basically the same thing. They just emphasize different aspects of the same concept.

- Inheritance-
	Inheritance allows one class, the "child" class, to inherit the properties and methods of another class, the "parent" class. it is a really bad idea to try to overuse it. Inheritance should only be used when all instances of a child class are also instances of the parent class. When a child class inherits from a parent, it inherits everything. If you only want to share some functionality, inheritance is probably not the best answer. Better to simply share some functions, or maybe make a new parent class that both classes can inherit from. Think of a VIN diagram. If you can fit the child class ENTIRELY into the parent class, then you should use inheritance. If not, you should think of other options.

- Polymorphism-
	While inheritance is the most unique trait of object-oriented languages, polymorphism is probably the most powerful. Polymorphism is the ability of a variable, function or object to take on multiple forms. `"poly"="many" "morph"="form"`. For example, classes in the same hierarchical tree may have methods with the same name but different behaviors. A function signature (or method signature) includes the name, inputs, and outputs of a function or method. Both methods have the same name, take 0 inputs, and return integers. If any of those things were different, they would have different function signatures. Calling two methods with the same signature should look the same to the caller. If you change the function signature of a parent class when overriding a method, it could be a disaster. The whole point of overriding a method is so that the caller of your code doesn't have to worry about what different things are going on inside the methods of different object types.
