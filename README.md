# 🧮 Python Math Operations Package
Welcome to the Math Operations Package, a simple and versatile Python library for performing essential mathematical operations! This package is designed to make arithmetic calculations and other math-related functionalities as easy as pie. 🥧

## 🚀 Features
- **Arithmetic Operations**: Perform addition, subtraction, multiplication, division and even many other complex operations with ease.
- **Friendly Outputs**: Results are displayed in a clear and user-friendly manner.
- **Expandable**: The structure is perfect for adding more mathematical functions over time.

## 📁 Project Structure
```
src/ 
├── maths_operations.py   # Contains all the mathematical functions 
tests/ 
├── test_operations.py    # Unit tests for the functions README.md # Documentation
```

## 🛠️ Installation
To get started, follow these steps:

1. **Clone the repository** to your local machine:

    ```bash
    git clone https://github.com/ArpitKadam/my-python-package.git
    cd MathOperationsPackage
    ```

2. No additional dependencies are required as this package uses only standard Python libraries. 🎉

3. (Optional) If you wish to install it as a package in your environment for easy usage, you can run:

    ```bash
    pip install .
    ```

## 📝 Usage
### Importing the Functions
After cloning the repository and navigating to the project folder, you can import the functions in your own Python project or script.

To use the functions, simply import them like this:

```python
from maths_operations import add, sub, mul, div, mod
```

## Examples
#### Addition
```python
add(5, 3)
```
- Output: The sum of a and b is: 8

#### Subtraction
```python
sub(10, 4)
```
- Output: The difference of a and b is: 6

#### Multiplication
```python
mul(7, 6)
```
- Output: The product of a and b is: 42

#### Division
```python
div(20, 4)
```
- Output: The division of a and b is: 5.0

## 📁 Folder Structure in Your Project
Once you’ve cloned the repository, here’s how you can organize it:

In your project, create a folder (e.g., ```my_project/```).

Inside your project folder, you can either copy the ```src/``` folder or install the package using ```pip install .``` to include it as a dependency.

To use the functions, import them like this:
```python
from my-python-package.src.maths_operations import add, sub, mul, div, mod
```

## 🧪 Running Tests
To run the tests included with the package, navigate to the ```tests/``` folder and run:

```bash
pytest tests
```
This will check if the functions work as expected and validate their functionality.

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request with your changes. If you have any ideas or issues, open a discussion or issue.

## 🌟 Acknowledgments

- Thanks to Python for being awesome.
- You, the user, for checking out this package!
