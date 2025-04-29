
import re
import requests
from bs4 import BeautifulSoup

url = "https://www.tutu.ru/view.php?np=2b22e616d4&date=26.04.2025"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Проверка на ошибки
    soup = BeautifulSoup(response.text, 'html.parser')
    stops = soup.find_all('td', class_='flag')
    id1 = soup.find_all('tr', 'select')
    working_days = soup.find_all('div', 'center_block movement_block')
    bow=[]
    for day in working_days:
        da = day.text.strip().split()
        bow = da
    works = (bow[-1])
    a=[]
    i=0
    arrive_time =[]
    for s in id1:
        a.append(s['id'])
        k=0
        raw_time = s.text.strip().split()
        for sd in raw_time[::-1]:
            c = re.search(r'\d{2}:\d{2}', sd)
            if c:
                arrive_time.append(c.group())
                k=1
                break
        if not k:
            arrive_time.append('Null')

    if not stops:
        print("Остановки не найдены. Возможно, изменилась структура сайта.")
    else:
        with open("stops.txt", "w", encoding="utf-8") as file:
            pars_results = []
            for sd in stops:
                stop_name = sd.get_text(strip=True)
                output = {'id' : a[i],
                          'station_name': stop_name,
                          'arrive_time' : arrive_time[i],
                          'station_number' : i+1}
                pars_results.append(output)
                i+=1
            file.write(str(pars_results))

        print("Список остановок сохранён в stops.txt")
except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")


