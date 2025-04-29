from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import psycopg2
import time
import random
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service

USER_AGENTS = open('user_agents.txt', 'r').readlines()
def brow():
    return webdriver.Chrome(service=Service('chromedriver.exe'), options=Options().add_argument(f'--user-agent={random.choice(USER_AGENTS)}'))


conn = psycopg2.connect(
    dbname="Train_Schedule", user="postgres", password="1234", host="localhost", port="5432"
)
cursor = conn.cursor()


url = "https://www.tutu.ru/station.php?nnst=101&date=30.04.2025"
driver = brow()
driver.get(url)
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

trains = soup.find_all('a', class_='link_e42f399a textBrand_b6f2fc7f gPG3tVjqDL4UJTcO')

trainid = 0

for train_div in trains:
    driver = brow()
    trainid += 1
    train_link = train_div.get('href')
    if not train_link:
        continue
    driver.get(train_link)
    time.sleep(0.1)
    train_soup = BeautifulSoup(driver.page_source, 'html.parser')
    stationOrder = 0
    records = train_soup.find_all('tr', class_='select')  # станции
    for record in records:
        tds = record.find_all('td')
        stationName = "'" + tds[1].text[1:-1] + "'"
        stationOrder += 1
        if tds[2].text.strip()[0:5] == '-':
            arrive_time = 'Null'
        else:
            arrive_time = "'" + tds[2].text.strip()[0:5] + "'"


        cursor.execute(
            f'INSERT INTO schedule_bel (trainid, stationname, Stationorder, arrive_time)'
            f'VALUES ({trainid}, {stationName}, {stationOrder}, {arrive_time})',
            )


conn.commit()
driver.quit()
conn.close()