# 🧾 Product Registration Automation (Python + PyAutoGUI)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Automation](https://img.shields.io/badge/Automation-PyAutoGUI-green)
![Data](https://img.shields.io/badge/Data-Pandas-orange)
![Status](https://img.shields.io/badge/Status-Educational%20Project-lightgrey)

This project demonstrates how to automate the process of **registering
products in a web system** using **GUI automation**.

The script automatically:

-   opens a browser
-   logs into a website
-   reads product data from a CSV file
-   fills a form
-   registers products automatically

The automation is implemented using **Python**, **PyAutoGUI**, and
**Pandas**.

------------------------------------------------------------------------

# 📂 Project Structure
```
.
├── script.py        # Main automation script
├── get-position.py  # Utility to capture mouse coordinates
├── products.csv     # Dataset containing products to register
└── README.md
```
------------------------------------------------------------------------

# ⚙️ How It Works

The automation follows these steps:

### 1️⃣ Open the browser

The script opens **Chrome** and navigates to the login page.

https://dlp.hashtagtreinamentos.com/python/intensivao/login

------------------------------------------------------------------------

### 2️⃣ Perform login

The automation fills in the login form automatically using
**PyAutoGUI**.

------------------------------------------------------------------------

### 3️⃣ Load product data

Product data is loaded from a CSV file using **Pandas**.

Example structure:
```
  Field            Description
  ---------------- --------------
  codigo           Product code
  marca            Brand
  tipo             Product type
  categoria        Category
  preco_unitario   Unit price
  custo            Cost
  obs              Notes
```
------------------------------------------------------------------------

### 4️⃣ Register products automatically

For each row in `products.csv`, the script:

1.  clicks the form fields
2.  types product information
3.  submits the form
4.  scrolls back to the top
5.  repeats the process

------------------------------------------------------------------------

# 🐍 Requirements

You must install **Python** before running this project.

Download it from the official website:

https://www.python.org/downloads/

During installation, make sure **"Add Python to PATH"** is enabled.

------------------------------------------------------------------------

# 📦 Install Required Libraries

The project depends on the following libraries:

-   PyAutoGUI → GUI automation
-   Pandas → CSV data processing

Install them with:
```bash
pip install pyautogui pandas
```
------------------------------------------------------------------------

# ▶️ Running the Automation

Run the main script:
```bash
python script.py
```
The automation will:

1.  Open Chrome
2.  Access the login page
3.  Log into the system
4.  Load the CSV dataset
5.  Register each product automatically

⚠️ Important: Do not move the mouse or use the computer while the
automation is running.

------------------------------------------------------------------------

# 🎯 Getting Mouse Coordinates

The automation interacts with the interface using **screen
coordinates**.

To identify coordinates on your screen, run:
```bash
python get-position.py
```
After running the script:

1.  Move the mouse to the desired location
2.  Wait 5 seconds
3.  The coordinates will be printed in the terminal

Example output:

Point(x=685, y=451)

You can then update the coordinates in `script.py`.

------------------------------------------------------------------------

# 📊 Example Dataset

Example from `products.csv`:
```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
MOLO000251,Logitech,Mouse,1,25.95,6.50,
CAHA000252,Hashtag,Camisa,2,25.00,11.00,Check stock
TELG000821,LG,Televisao,1,820.00,172.20,
```
Each row represents a product that will be automatically registered in
the system.

------------------------------------------------------------------------

# ⚠️ Important Notes

-   This script uses **screen coordinates**, which may vary depending
    on:

    -   screen resolution
    -   browser size
    -   operating system

-   Coordinates may need to be adjusted before running the automation.

-   Avoid interacting with the computer during execution.

------------------------------------------------------------------------

# 🎓 Educational Purpose

This project was created to demonstrate:

-   Python automation
-   GUI scripting
-   CSV data processing
-   practical usage of PyAutoGUI

------------------------------------------------------------------------

# 📜 License

This project is intended for **learning and demonstration purposes**.

------------------------------------------------------------------------

⭐ If this project helped you learn Python automation, consider giving
the repository a star!
