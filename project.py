# Rewrite
import requests, os, time
from datetime import datetime


class City:
    cities = {
        "North": {
            "Taipei City": "臺北市",
            "New Taipei City": "新北市",
            "Keelung City": "基隆市",
            "Ylian County": "宜蘭縣",
            "Taoyuan City": "桃園市",
            "Hsinchu City": "新竹市",
            "Hsinchu County": "新竹縣",
        },
        "East": {
            "Hualien County": "花蓮縣",
            "Taitung County": "臺東縣",
        },
        "West": {
            "Miaoli County": "苗栗縣",
            "Taichung City": "臺中市",
            "Changhua County": "彰化縣",
            "Nantou County": "南投縣",
            "Yunlin County": "雲林縣",
        },
        "South": {
            "Chiayi City": "嘉義市",
            "Chiayi County": "嘉義縣",
            "Tainan City": "臺南市",
            "Kaohsiung City": "高雄市",
            "Pingtung County": "屏東縣",
        },
        "Offshore islands": {
            "Penghu County": "澎湖縣",
            "Kinmen County": "金門縣",
            "Lienchiang County": "連江縣",
        },
    }

    @classmethod
    def show_area(cls):
        temp = ""
        for area in cls.cities.keys():
            temp += area + ", "
        return temp.rstrip(", ")

    @classmethod
    def show_cities(cls, area):
        os.system("clear")
        temp = ""
        for city in cls.cities[area]:
            temp += city + ", "
        return temp.rstrip(", ")


def main():
    ...


def area_validator(area_name):
    c_area_name = area_name.capitalize()
    if c_area_name not in City.cities.keys():
        raise ValueError
    return c_area_name


def city_validator(area_name, city_name):
    c_city_name = city_name.capitalize()
    if c_city_name not in City.cities[area_name].keys():
        raise ValueError
    return City.cities[area_name][c_city_name]


def get_data(city_name):
    now = datetime.now()
    result = requests.get(
        f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-6665EC6B-FF52-499B-AA73-B9CDE98D905D&format=JSON&locationName={city_name}&elementName=PoP&timeFrom={now}"
    )
    the_record = result.json()["records"]["location"][0]["weatherElement"][0]["time"][0]
    start_time = the_record["startTime"].split(" ")[1].split(":")[0]
    end_time = the_record["endTime"].split(" ")[1].split(":")[0]
    pop = the_record["parameter"]["parameterName"]

    return f"The pop for the {city_name} today, from {start_time} to {end_time} is {pop}%."


if __name__ == "__main__":
    main()
