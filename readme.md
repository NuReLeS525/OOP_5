# Electronic Store Management System

A Python-based electronic store management system that allows users to browse devices, add items to a shopping cart, and complete purchases. The system demonstrates object-oriented programming principles including inheritance, encapsulation, and polymorphism.

## 📋 Table of Contents
- [Features](#features)
- [Class Structure](#class-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Input/Output](#sample-inputoutput)
- [Running Tests](#running-tests)
- [UML Class Diagram](#uml-class-diagram)
- [License](#license)

## ✨ Features

- **Device Management**: Browse available electronic devices with detailed specifications
- **Shopping Cart**: Add multiple items with quantity validation
- **Inventory Management**: Automatic stock reduction after checkout
- **Discount System**: Apply discounts to any device
- **Three Device Types**:
  - Smartphones (with screen size and battery life)
  - Laptops (with RAM and processor speed)
  - Tablets (with screen resolution and weight)

## 🏗️ Class Structure

### Base Class: `Device`
The parent class for all electronic devices with common attributes and methods.

**Attributes:**
- `name` (str): Device name
- `price` (float): Device price
- `stock` (int): Available quantity
- `warranty_period` (int): Warranty period in months

**Methods:**
- `display_info()`: Returns device information as formatted string
- `apply_discount(discount_percentage)`: Reduces price by given percentage
- `is_available(amount)`: Checks if requested quantity is in stock
- `reduce_stock(amount)`: Reduces stock by specified amount

### Child Classes

#### `Smartphone(Device)`
**Additional Attributes:**
- `screen_size` (float): Screen size in inches
- `battery_life` (int): Battery life in hours

**Additional Methods:**
- `make_call()`: Simulates making a call
- `install_app()`: Simulates app installation

#### `Laptop(Device)`
**Additional Attributes:**
- `ram_size` (int): RAM size in GB
- `processor_speed` (float): Processor speed in GHz

**Additional Methods:**
- `run_program()`: Simulates running a program
- `use_keyboard()`: Simulates typing

#### `Tablet(Device)`
**Additional Attributes:**
- `screen_resolution` (str): Screen resolution (e.g., "2388x1668")
- `weight` (int): Weight in grams

**Additional Methods:**
- `browse_internet()`: Simulates web browsing
- `use_touchscreen()`: Simulates touch interaction

### `Cart` Class
Manages shopping cart operations.

**Attributes:**
- `items` (list): List of tuples (device, quantity)
- `total_price` (float): Total cost of items in cart

**Methods:**
- `add_device(device, amount)`: Adds device to cart with stock validation
- `get_total_price()`: Returns total cart value
- `print_items()`: Displays all items in cart
- `checkout()`: Processes purchase and updates inventory

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/electronic-store-system.git
cd electronic-store-system