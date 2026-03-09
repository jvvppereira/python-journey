import pyautogui
import time

pyautogui.FAILSAFE = True # default behavior of pyautogui
pyautogui.PAUSE = 0.3

URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
BROWSER = "chrome"
FIELDS = ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo", "obs"]

# Step 01: Open URL
# open chrome browser
pyautogui.press("win")
pyautogui.write(BROWSER)
pyautogui.press("enter")

# type the URL and press enter
time.sleep(3)
pyautogui.write(URL)
pyautogui.press("enter")
time.sleep(3)

# Step 02: Do the login
# pyautogui.click(x=738, y=368) # click on the email field based on the position of the mouse
pyautogui.press("tab")
pyautogui.write("test@email.com")
pyautogui.press("tab") # to focus on the next field
pyautogui.write("9f3c0b7a-cc2e-4e2a-8c0e-7b2a6c6d6c2e")
pyautogui.press("tab")
pyautogui.press("space") # to click on the login button
time.sleep(3)

# Step 03: import the table with the products to be registered
import pandas as pd

table = pd.read_csv("products.csv")
# print(table)

# Step 04: register the products in the system
for row in table.index:
    pyautogui.click(x=740, y=261) # click on the code field based on the position of the mouse
    
    for field in FIELDS:
        value = table.loc[row, field]
        isObs = field == "obs"
        shouldWrite = not isObs or (not pd.isna(value) and isObs)
        if shouldWrite:
            pyautogui.write(str(value))
        pyautogui.press("tab")

    pyautogui.press("enter") # register the product
    pyautogui.scroll(5000)# scroll up to the top of the page to register the next product
    # Step 05: repeat the process for all products in the table
