import pyautogui
import time

pyautogui.FAILSAFE = True # default behavior of pyautogui
pyautogui.PAUSE = 0.3

URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
BROWSER = "chrome"

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

# click on the email field based on the position of the mouse
# pyautogui.click(x=738, y=368)
pyautogui.press("tab")
# type the email and password
pyautogui.write("test@email.com")
pyautogui.press("tab") # to focus on the password field
pyautogui.write("9f3c0b7a-cc2e-4e2a-8c0e-7b2a6c6d6c2e")
pyautogui.press("tab")
pyautogui.press("space") # to click on the login button
time.sleep(3)

# Step 03: import the table with the products to be registered
import pandas as pd

table = pd.read_csv("products.csv")
# print(table)

# Step 04: register the products in the system
for linha in table.index:
    # click on the code field based on the position of the mouse
    pyautogui.click(x=740, y=261)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = table.loc[linha, "codigo"]
    # fill the code field
    pyautogui.write(str(codigo))
    # move to the next field
    pyautogui.press("tab")
    # fill the brand field
    pyautogui.write(str(table.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = table.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(table.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # register the product
    # scroll up to the top of the page to register the next product
    pyautogui.scroll(5000)
    # Step 05: repeat the process for all products in the table
