
# % Discount Calculator Lab 

In this Lab building a discount calculator, I learnt how to design flexible and maintainable software using **Object-Oriented Programming (OOP)** principles in Python.

The goal of the lab was to apply different discount strategies to a product and calculate the **best possible price** for a user.

## 🎯 Project Overview

This program:

* Creates a `Product`
* Applies multiple discount strategies
* Checks which discounts are applicable
* Calculates all possible discounted prices
* Returns the **lowest (best) price**

Example output:

```bash
Best price for Wireless Mouse for Premium user: $40.00
```


##  Key Lessons & Takeaways

### 1️⃣ Object-Oriented Programming (OOP)

I practiced structuring a program using classes:

* `Product`
* `DiscountStrategy`
* `PercentageDiscount`
* `FixedAmountDiscount`
* `PremiumUserDiscount`
* `DiscountEngine`

This helped me understand how to model real-world problems using objects.


### 2️⃣ Abstract Base Classes (ABC)

Using:

```python
from abc import ABC, abstractmethod
```

I learned how to:

* Create an abstract class (`DiscountStrategy`)
* Force subclasses to implement required methods
* Build consistent and predictable class structures

This improves reliability and code structure.


### 3️⃣ Strategy Design Pattern

This lab introduced me to the **Strategy Pattern**.

Instead of writing all discount logic in one place, I created separate discount classes and passed them into the `DiscountEngine`.

  This makes the system:

* Flexible
* Easy to extend
* Easy to maintain

If I want to add a new discount type, I just create a new class — no need to modify existing code.


### 4️⃣ Polymorphism

Each discount class implements:

* `is_applicable()`
* `apply_discount()`

Even though each class behaves differently, the `DiscountEngine` treats them the same way.

This is called **polymorphism**, and it makes the system clean and scalable.


### 5️⃣ Separation of Responsibilities

Each class has a clear role:

| Class               | Responsibility                    |
| ------------------- | --------------------------------- |
| `Product`           | Stores product data               |
| `DiscountStrategy`  | Defines discount blueprint        |
| Discount subclasses | Implement specific discount logic |
| `DiscountEngine`    | Calculates the best price         |

This structure keeps the code organized and professional.


### 6️⃣ Type Hinting

Using:

```python
from typing import List
```

and defining return types like:

```python
def calculate_best_price(...) -> float:
```

helped make the code:

* More readable
* Easier to debug
* More maintainable


##  Skills Strengthened

* Writing scalable OOP code
* Applying design patterns
* Using abstraction properly
* Implementing polymorphism
* Designing clean software architecture

---

## Final Reflection

This lab helped me move from writing simple scripts to designing structured systems using real software engineering principles.

It strengthened my understanding of:

* Abstraction
* Polymorphism
* Encapsulation
* Clean architecture design

---

💡 *This project represents a strong step forward in writing professional, extensible Python code.*

