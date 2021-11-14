from time import sleep
import pyfiglet as fig

from colorama import Fore, Style

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.driver import ChromeDriver

from const import USER, PASS
import datetime
import time
import os

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

os.system("cls")
def author():
    print(Fore.BLUE + "==========================================================================")
    style = fig.figlet_format("          Shopee  Bot")
    print(style)
    style = fig.figlet_format("           ARITTO999")
    print(style)
    print("==========================================================================" + Fore.RESET)
    print(Fore.RED + Style.BRIGHT + "For product with multi variation value of variation 1 and 2 is Case - Sensitive")
    print("If product only have 1 variation criteria please, fill [ - ] in variation 2" + Style.RESET_ALL + Fore.RESET)

global flashTime
global uriLink
global multiVar
global var1
global var2

def openBrowser():
    driver.get('https://shopee.co.id/buyer/login')
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    
    doLogin()

def doLogin():
    login = False
    userInput = WebDriverWait(driver,1200).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name='loginKey']")))
    passInput = WebDriverWait(driver,1200).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name='password']")))
    userInput.send_keys(USER)
    passInput.send_keys(PASS)
    sleep(2)
    btnLogin = WebDriverWait(driver,1200).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/button")))
    btnLogin.click()
    while login==False:
        print(Fore.CYAN + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.YELLOW + "Menunggu proses login")
        if checkElementByClass("shopee-avatar__img")==True:
            login = True
            automateFlashSale()

def automateFlashSale():
    while datetime.datetime.now() <= flashTime:
        print(Fore.CYAN + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.YELLOW + "Flash Sale Belum Mulai")
    print(Fore.YELLOW + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.GREEN + "Openning product page")
    transaksiBeli();

def transaksiBeli():
    driver.get(uriLink)
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    print(Fore.YELLOW + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.GREEN + "Waiting product page load")

    #Check product variaion
    if multiVar == "Y" or multiVar == "y":
        if var1 != "-":
            try:
                print(Fore.CYAN + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.YELLOW + "Search variation 1 object" + Fore.RESET)
                var1Elms = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[text()='" + var1 +"']")))
                var1Elms.click()
            except ElementNotVisibleException:
                print(Fore.RED + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.RED + "No variation 1 with value " + var1 + Fore.RESET)
            except TimeoutException:
                print(Fore.RED + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.RED + "No variation 1 with value " + var1 + Fore.RESET)    
        if var2 != "-":
            try:
                print(Fore.CYAN + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.YELLOW + "Search variation 2 object" + Fore.RESET)
                var2Elms = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[text()='" + var2 +"']")))
                var2Elms.click()
            except ElementNotVisibleException:
                print(Fore.RED + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.RED + "No variation 2 with value " + var2 + Fore.RESET)
            except TimeoutException:
                print(Fore.RED + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.RED + "No variation 2 with value " + var2 + Fore.RESET)    

    
    btnBeli = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//*[@id='main']/div/div[2]/div[2]/div/div[1]/div[3]/div/div[5]/div/div/button[2]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", btnBeli)
    btnBeli.click()
    print(Fore.YELLOW + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.GREEN + "Stuff already in cart")
    print(Fore.YELLOW + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.GREEN + "Continue Checkout Process")
    checkOut()

def checkOut(): 
    print(Fore.YELLOW + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.GREEN + "Waiting for checkout")
    btnCheckout = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.shopee-button-solid.shopee-button-solid--primary")))
    #btnCheckout = WebDriverWait(driver,120).until(EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div/div[2]/div[2]/div/div[3]/div[2]/div[7]/button[4]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", btnCheckout)
    btnCheckout.click()
    print(Fore.YELLOW + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.GREEN + "Continue to payment process")
    payment()

def payment():
    print(Fore.YELLOW + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.GREEN + "Waiting payment page ready")
    btnMethod = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,"//button[text()='Indomaret / i.Saku']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", btnMethod)
    btnMethod.click()
    btnPayment = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button.stardust-button.stardust-button--primary.stardust-button--large")))
    driver.execute_script("arguments[0].scrollIntoView(true);", btnPayment)
    btnPayment.click()
    print(Fore.YELLOW + "[",datetime.datetime.now(),"]" + Fore.RESET +" => " + Fore.GREEN + "Stuff ready to pay!")
    author()
    sleep(60)
    driver.quit()

def checkElementByClass(classname):
    try:
        driver.find_element(By.CLASS_NAME,classname)
        return True
    except NoSuchElementException:
        return False
        
author()
uriLink = input("Product link : " + Fore.GREEN)
time = input(Fore.RESET + "Flash sale time start (yy-mm-dd hh:mm:ss) : " + Fore.RED)
multiVar = input(Fore.RESET + "Product variation (Y / T) : " + Fore.GREEN)
if multiVar == "Y" or multiVar == "y":
    var1 = input(Fore.RESET + "Variation 1 value (ex color, size, etc) : " + Fore.RED)
    var2 = input(Fore.RESET + "Variation 2 value (ex color, size, etc) : " + Fore.RED)
flashTime = datetime.datetime.strptime(time, "%y-%m-%d %H:%M:%S")
sel = datetime.datetime.now() - flashTime
print(Fore.RESET + "Sisa waktu flash sale : " + Fore.RED,sel,""+Fore.RESET)
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
#options.headless = True
options.add_argument(f'user-agent={user_agent}')
#options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
#options.add_argument("--proxy-server='direct://'")
#options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
prefs = {'profile.default_content_setting_values': {'images': 2,
                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                            'durable_storage': 2}}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
#option = webdriver.ChromeOptions()
#option.add_argument('--start-maximized')
#driver = webdriver.Chrome('chromedriver.exe', options=option)
openBrowser()