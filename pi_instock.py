from bs4 import BeautifulSoup
import requests, json, threading


class scrape:
    def __init__(self):

        self.links = json.load(open("urls.json", "r"))
        
        self.found = []


    def check(self) -> list:

        func_map = [
            self.pi_shop,
            self.adafruit,
            self.vilros
        ]

        threads = []
        
        for func in func_map:

            t = threading.Thread(target=func)
            t.start()

            threads.append(t)

        for thread in threads:
            thread.join()
            
        print(self.found)

        
    def grab_page(self, url):

        return BeautifulSoup(requests.get(url).content, "html.parser")
    

    #=================================[Websites]=======================================#

    def adafruit(self):

        print("Checking adafruit")
        for link in self.links["adafruit"]:

            parser = self.grab_page(link)
            stock = parser.find(attrs={"itemprop": "availability"})

            if stock.text != "Out of stock":
                self.found.append(link)


    def pi_shop(self):

        print("Checking Pi Shop")
        for link in self.links["pi_shop"]:

            parser = self.grab_page(link)
            stock = parser.find("input", {"id": "form-action-addToCart"}).get_attribute_list("value")[0]

            if stock != "Out of stock":
                self.found.append(link)
    

    def vilros(self):

        print("Checking vilros")
        for link in self.links["vilros"]:

            parser = self.grab_page(link)
            
            try:
                stock = parser.find("button", {"name": "add"}).findChild("span").text
            except Exception:
               pass

            if "Sold Out" not in stock:
                self.found.append(link)
            
    
   