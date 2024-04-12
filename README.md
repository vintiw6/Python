<style>
  .title {
    font-size: 2em;
    color: #333;
    text-align: center;
  }

  .description {
    font-style: italic;
    padding: 1em;
  }

  .content h2 {
    font-size: 1.5em;
    margin-bottom: 0.5em;
  }

  .concept, .example {
    margin-bottom: 1em;
  }

  .concept code, .example code {
    font-family: monospace;
    background-color: #f5f5f5;
    padding: 0.5em 1em;
    border-radius: 3px;
  }
</style>

<h1 class="title">My Python Learning Journey</h1>

<p class="description">This repository documents my exploration of the Python programming language. It serves as a record of my progress and a resource for anyone interested in learning Python.</p>

<div class="content">

  ## Core Concepts

  This section covers the fundamental building blocks of Python programming:

  **Variables and Data Types**

  Variables store data, and data types define the kind of data a variable can hold. Explore basic data types like integers, floats, strings, booleans, and None.

  ```python
  # Integer
  age = 25

  # Float (decimal number)
  pi = 3.14159

  # String (text)
  name = "Alice"

  # Boolean (True or False)
  is_raining = False

  # None (represents absence of a value)
  empty_variable = None

  print(age, pi, name, is_raining, empty_variable)
