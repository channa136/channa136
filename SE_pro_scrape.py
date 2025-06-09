import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(filename="SEpro.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def webopener():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  ## Enable headless
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        options.page_load_strategy= "eager"
        options.add_argument("--disable-blink-features=AutomationControlled")  
        driver_service = Service(executable_path = r"C:\Users\Hadid haider channa\chromedriver.exe")
        driver= webdriver.Chrome(service=driver_service , options=options)
        driver.set_page_load_timeout(30)
        driver.get("https://www.livecoinwatch.com/")
        logging.info("WEB succefully opened")
        print("web opening success")
        time.sleep(30)
        return driver
    except Exception or TypeError or NameError as e:
        logging.error(f"error : {e}")
        print(f"error : {e}")
        

def webscraper():
    driver=webopener()
    names=[]
    prices=[]
    volumes=[]
    try:
        cookiesbtn= WebDriverWait(driver , 30).until(
            EC.element_to_be_clickable((By.XPATH ,"//span[@class='btn btn-main btn-accept']"))
        )
        cookiesbtn.click()
        
        coins =WebDriverWait(driver , 30).until(
            EC.presence_of_all_elements_located((By.XPATH ,"//tr[@class='table-row filter-row']"))
        )
        print(f"found {len(coins)} results")
        for i,coin in enumerate(coins,1):
            name = coin.find_element(By.XPATH ,".//div[@class='item-name ml10']/div").text.strip()
            names.append(name)
            price = coin.find_element(By.XPATH ,".//td[@class='filter-item table-item main-price']").text
            prices.append(price)
            volume=coin.find_element(By.XPATH ,".//td[@class='filter-item table-item volume price']").text
            volumes.append(volume)
        logging.info(f"Data succefully scraped")
        return names,prices,volumes
    except Exception or TypeError or NameError as e:
        logging.error(f"error : {e}")
        print(f"error : {e}")

#data = webscraper()        