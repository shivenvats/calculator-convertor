# Project Statement

## Problem Statement

People often need quick everyday calculations and unit conversions: basic arithmetic, checking their BMI, converting a temperature, or changing a speed from km/h to mph or m/s. These tasks usually mean opening several different websites or apps, or doing the maths by hand, which is slow and easy to get wrong (for example, using the wrong BMI ranges or the wrong conversion formula).

This project provides a single, simple, offline tool that brings these tasks together in one menu-driven Python application, with correct formulas and clear results.

## Scope of the Project

**In scope**
- A console (command-line) application written in Python.
- A calculator for addition, subtraction, multiplication and division.
- Converters for BMI, temperature (Celsius to Kelvin and Fahrenheit) and speed (km/h to mph and m/s).
- A main menu that lets the user repeat tasks until they choose to exit.
- Handling of invalid menu choices, invalid operators and division by zero.

**Out of scope**
- A graphical or web interface.
- Online data, user accounts or database storage.
- Scientific or advanced mathematical functions.

## Target Users

- Students who need quick calculations and conversions.
- Beginners learning Python who want a clear example of a modular, menu-driven program.
- Anyone who wants a simple offline calculator and converter without installing large software.

## High-Level Features

1. **Calculator module**: performs the four basic arithmetic operations on decimal numbers and safely handles division by zero.
2. **BMI module**: calculates BMI from height and weight and classifies it into Underweight, Healthy Weight, Overweight or Obesity Class 1, 2 or 3.
3. **Temperature module**: converts a Celsius value to Kelvin and Fahrenheit.
4. **Speed module**: converts a speed in km/h to mph and m/s.
5. **Main menu**: one entry point that connects all modules, validates the user's choice and loops until the user exits.
