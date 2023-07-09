import requests
from bs4 import BeautifulSoup
from flipkart_db import DbModel


class Scrapper(object):
    BASE_URL = "https://www.example.com/mobiles"  # Replace with the actual URL

    def get_page_content(self):
        """
        Get the page content
        :return:
        """
        response = requests.get(self.BASE_URL, headers={"USER-AGENT": "MOZILLA/5.0"})
        return response.content

    def parse_content(self):
        """
        Parse the content and return the list of mobiles
        :return:
        """
        content = self.get_page_content()
        html_content = BeautifulSoup(content, "html.parser")
        mobiles = html_content.find_all("div", {"class": "mobile"})
        result = []
        for mobile in mobiles:
            result.append({
                "model": str(mobile.find("div", {"class": "model"}).text).replace("\n", ""),
                "price": str(mobile.find("div", {"class": "price"}).text).replace("\n", ""),
                "rating": str(mobile.find("div", {"class": "rating"}).text).replace("\n", ""),
                "image": mobile.find("img")["src"],
                "description": str(mobile.find("div", {"class": "description"}).text).replace("\n", ""),
                "reviews": str(mobile.find("div", {"class": "reviews"}).text).replace("\n", ""),
                "specifications": str(mobile.find("div", {"class": "specifications"}).text).replace("\n", "")
            })
        return result

    def insert_to_db(self):
        db_model = DbModel('mobiles.db')
        db_model.connect()
        db_model.create_table()
        db_data = db_model.get_all_mobile_names()
        if len(db_data) > 0:
            db_data = [d[0] for d in db_data if len(d) > 0]
        print("DB Data: ", db_data)
        mobiles = self.parse_content()
        for mobile in mobiles:
            if mobile.get("model") not in db_data:
                db_model.cursor.execute('''
                    INSERT INTO mobiles (model, price, rating, image, description, reviews, specifications)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    mobile.get("model"),

