import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

def get_neste_dizelis(url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for row in soup.find_all("tr"):
        cols = row.find_all(["td", "th"])
        if len(cols) >= 3 and "Neste Futura D" in cols[0].text:
            cena = cols[1].text.strip().replace(",", ".")
            vieta = cols[2].text.strip()
            return cena, vieta
        elif len(cols) >= 2 and "Neste Futura D" in cols[0].text:
            cena = cols[1].text.strip().replace(",", ".")
            return cena, "Nav norādīts"
    return None, None

def get_circlek_dizelis(url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for row in soup.find_all("tr"):
        cols = row.find_all(["td", "th"])
        # Precīzi meklē pēc "Dmiles" (ar lielo D)
        if len(cols) >= 3 and cols[0].text.strip() == "Dmiles":
            cena = cols[1].text.strip().replace(",", ".").replace(" EUR", "")
            vieta = cols[2].text.strip()
            return cena, vieta
    return None, None

def get_viada_dizelis(url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
    soup = BeautifulSoup(driver.page_source, "html.parser")
    rows = soup.find_all("tr")
    if len(rows) >= 5:
        cols = rows[4].find_all(["td", "th"])  # 5. rinda (indekss 4)
        if len(cols) >= 3:
            cena = cols[1].text.strip().replace(",", ".")
            vieta = cols[2].text.strip()
            return cena, vieta
        elif len(cols) >= 2:
            cena = cols[1].text.strip().replace(",", ".")
            return cena, "Nav norādīts"
    return None, None

neste_url = "https://www.neste.lv/lv/content/degvielas-cenas"
circlek_url = "https://www.circlek.lv/degviela-miles/degvielas-cenas"
viada_url = "https://www.viada.lv/zemakas-degvielas-cenas/"

neste_dizelis, neste_vieta = get_neste_dizelis(neste_url)
circlek_dizelis, circlek_vieta = get_circlek_dizelis(circlek_url)
viada_dizelis, viada_vieta = get_viada_dizelis(viada_url)

driver.quit()

print("Aktuālās dīzeļdegvielas cenas:")
if neste_dizelis:
    print(f"Neste: {neste_dizelis} €/L ({neste_vieta})")
else:
    print("Neste cena nav pieejama.")

if circlek_dizelis:
    print(f"Circle K: {circlek_dizelis} €/L ({circlek_vieta})")
else:
    print("Circle K cena nav pieejama.")

if viada_dizelis:
    print(f"Viada: {viada_dizelis} €/L ({viada_vieta})")
else:
    print("Viada cena nav pieejama.")