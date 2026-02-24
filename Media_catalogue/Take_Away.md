# 🎬 Media Catalogue Lab 🎬

In this Lab building a Media Catalogue system, I learnt how to design structured and reliable software using **Object-Oriented Programming (OOP)** concepts such as inheritance, custom exceptions, validation, and polymorphism.

The goal of the lab was to create a catalogue that can store both **Movies** and **TV Series**, while enforcing validation rules and handling errors properly.

---

## 🎯 Project Overview

This program:

* Defines a `Movie` parent class
* Extends it using a `TVSeries` child class
* Creates a `MediaCatalogue` to store media items
* Implements validation for correct data
* Uses custom exceptions for better error handling
* Displays categorized output (Movies vs TV Series)

Example output:

```bash
Media Catalogue (4 items):

=== MOVIES ===
1. The Matrix (1999) - 136 min, The Wachowskis
2. Inception (2010) - 148 min, Christopher Nolan

=== TV SERIES ===
1. Scrubs (2001) - 9 seasons, 182 episodes, 24 min avg, Bill Lawrence
2. Breaking Bad (2008) - 5 seasons, 62 episodes, 47 min avg, Vince Gilligan
```

---

## 📚 Key Lessons & Takeaways

### 1️⃣ Object-Oriented Programming (OOP)

I structured the system using classes:

* `Movie`
* `TVSeries`
* `MediaCatalogue`
* `MediaError`

This helped me model real-world entities using objects and relationships.


### 2️⃣ Inheritance

`TVSeries` inherits from `Movie`:

```python
class TVSeries(Movie):
```

This allowed me to:

* Reuse existing code from `Movie`
* Extend functionality with new attributes (`seasons`, `total_episodes`)
* Avoid code duplication

This is a clean and powerful use of inheritance.


### 3️⃣ Input Validation

Inside constructors, I added validation rules:

* Title cannot be empty
* Year must be 1895 or later
* Duration must be positive
* Seasons and episodes must be valid numbers

This taught me that **data validation is essential** when designing reliable systems.


### 4️⃣ Custom Exceptions

I created a custom exception:

```python
class MediaError(Exception):
```

This helped me:

* Raise meaningful errors
* Attach the invalid object to the exception
* Improve debugging and user feedback

Instead of generic errors, the system now provides structured and informative error messages.


### 5️⃣ Polymorphism

Because `TVSeries` inherits from `Movie`, the catalogue can treat both as media items.

This allows:

```python
isinstance(media_item, Movie)
```

The catalogue accepts both Movies and TV Series without separate logic.

This is practical polymorphism in action.

---

### 6️⃣ Type Checking & Instance Checking

Using:

```python
isinstance()
type()
```

helped me understand:

* The difference between exact type checking (`type(item) is Movie`)
* Inheritance-aware checking (`isinstance(item, TVSeries)`)

This is important when working with class hierarchies.


### 7️⃣ Clean Class Responsibilities

Each class has a clear purpose:

| Class            | Responsibility                          |
| ---------------- | --------------------------------------- |
| `Movie`          | Represents a movie                      |
| `TVSeries`       | Extends Movie with series-specific data |
| `MediaCatalogue` | Stores and organizes media items        |
| `MediaError`     | Handles media-related errors            |

This separation makes the system organized and scalable.


##  Skills Strengthened

* Class design
* Inheritance
* Constructor validation
* Custom exceptions
* Polymorphism
* Clean output formatting
* Structured error handling


## Final Reflection

This lab helped me understand how to:

* Build systems with parent-child relationships
* Protect data integrity with validation
* Handle errors professionally
* Organize objects inside collections
* Design clean and maintainable architecture

It strengthened my ability to write software that is not only functional but also structured like real-world production systems.

---

💡 *This project represents growth in building object-oriented systems with validation and proper exception handling.*
