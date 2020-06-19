# SOLID 
is a mnemonic abbreviation for a set of design principles created for software development in object-oriented languages. The principles in SOLID are intended to foster simpler, more robust and updatable code from software developers. Each letter in SOLID corresponds to a principle for development:

Why do you need to know?
1. Easy to understand the codebase
2. Easy to extend
3. Easy to maintain the codebase
4. Robust code
5. Minimum changing existing codebase or not at all.

## 1.Single Responsibility Principle
The Single Responsibility Principle requires that a class should have only one job. So if a class has more than one responsibility, it becomes coupled. A change to one responsibility results to modification of the other responsibility.

## 2.Open-Closed Principle
Software entities(Classes, modules, functions) should be open for extension, not modification.

## 3.Liskov Substitution Principle
The main idea behind Liskov Subtitution Principle is that, for any class, a client should be able to use any of its subtypes indistinguishably, without even noticing, and therefore without compromising the expected behavior at runtime. This means that clients are completely isolated and unaware of changes in the class hierarchy.

## 4.Interface Segregation Principle
Make fine grained interfaces that are client specific Clients should not be forced to depend upon interfaces that they do not use. This principle deals with the disadvantages of implementing big interfaces.