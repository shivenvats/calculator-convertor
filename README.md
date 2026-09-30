# Calculator & Converter

A menu-driven Python console application that combines a basic arithmetic calculator with three everyday converters: BMI, temperature and speed.

Built as the **VITyarthi – Build Your Own Project** submission.

## Overview

The program starts with a main menu where the user chooses between calculating and converting. Each feature lives in its own module, takes input from the keyboard, validates it, and prints a clear result. After every task the user returns to the main menu until they choose to exit.

## Features

- **Calculator**: addition, subtraction, multiplication and division of two numbers (decimals supported).
- **BMI calculator**: takes age, height (metres) and weight (kg), then reports the BMI value and its category (Underweight, Healthy Weight, Overweight, Obesity Class 1/2/3).
- **Temperature converter**: converts Celsius to Kelvin and Fahrenheit.
- **Speed converter**: converts km/h to mph and m/s.
- **Error handling**: invalid menu choices, invalid operators and division by zero are handled without crashing.
- **Menu loop**: the user can perform many operations in one session and exit cleanly.

## Technologies Used

- Python 3.10 or above (uses the `match` statement)
- Git and GitHub for version control

No external libraries are needed.

## Project Structure

```
calculator-convertor/
├── main_menu.py      # Entry point: welcome banner and main menu
├── calculator.py     # cal(): arithmetic operations
├── bmi.py            # bmi(): BMI calculation and classification
├── temperature.py    # temprature(): Celsius to Kelvin/Fahrenheit
├── speed_01.py       # s(): km/h to mph and m/s
├── statement.md      # Problem statement, scope, users, features
├── README.md
└── .gitignore
```

## How to Install and Run

1. Install Python 3.10 or newer from [python.org](https://www.python.org/downloads/).
2. Clone the repository:
   ```
   git clone https://github.com/shivenvats/calculator-convertor.git
   cd calculator-convertor
   ```
3. Run the program:
   ```
   python main_menu.py
   ```

## How to Use

```
1) CALCULATE
2) CONVERTOR
3) EXIT
```

- Choose **1** to calculate, then pick an operator (a = +, b = -, c = *, d = /) and enter two values.
- Choose **2** to convert, then pick a = BMI, b = Temperature or c = Speed.
- Choose **3** to exit.

## Instructions for Testing

The project is tested manually. Run `python main_menu.py` and try the cases below.

| # | Feature | Input | Expected output |
|---|---------|-------|-----------------|
| 1 | Calculator | Choice `1`, operator `a`, x = `5`, y = `3` | `x + y = 8.0` |
| 2 | Calculator | Choice `1`, operator `d`, x = `5`, y = `0` | `Cannot divide by zero` |
| 3 | Calculator | Choice `1`, operator `z` | `Invalid Operator` |
| 4 | BMI | Age `20`, height `1.70`, weight `65` | `22.49 , Healthy Weight` |
| 5 | BMI | Age `20`, height `1.70`, weight `100` | `34.60 , Obesity (Class 1)` |
| 6 | Temperature | `36.6` Celsius | `kelvin = 309.75k`, `Fahrenheit = 97.88F` (approx.) |
| 7 | Speed | `90` kmph | `speed_mph = 55.89mph`, `speed_mps = 25.0mps` |
| 8 | Main menu | Choice `9` or `abc` | `Invalid Response`, menu shown again |
| 9 | Main menu | Choice `3` | `Have a Nice Day!!!` and the program ends |

## Screenshots

_Add screenshots of the main menu, a calculation, and each converter here._

```
![Main menu](screenshots/main_menu.png)
![BMI result](screenshots/bmi.png)
```

## Known Limitations and Future Work

- Non-numeric input inside the calculator and converters (for example typing letters for height) is not yet validated.
- Add more converters (length, weight, currency).
- Save calculation history to a file.
- Add automated unit tests with `pytest` and logging.

## Author

**Name:** _your name_
**Registration No.:** _your registration number_
**GitHub:** [shivenvats](https://github.com/shivenvats)
