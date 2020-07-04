from bs4 import BeautifulSoup
import requests

base_url = 'https://www.jumia.com.eg/mobile-phones/'
realmeFile = open('C:\\Users\\omnia\\Documents\\scrap\\realme.txt', 'w')
samsungFile = open('C:\\Users\\omnia\\Documents\\scrap\\samsung.txt', 'w')
huaweiFile = open('C:\\Users\\omnia\\Documents\\scrap\\huawei.txt', 'w')
xiaomiFile = open('C:\\Users\\omnia\\Documents\\scrap\\xiaomi.txt', 'w')
count = 0


class Mobile(object):
    def __init__(self, url, file):
        self.url = url
        self.file = file

    def scrap(self):
        global count
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml')
        cards = soup.find_all('article', class_='prd _fb col c-prd')
        for card in cards:
            info = card.find('h3', class_='name').text.strip('\n')
            price = card.find('div', class_='prc').text
            txt = '{}  {}{}'.format(info, " its price ->", price)
            self.file.write(txt)
            self.file.write("\n")
            count += 1


class List_Mobile(Mobile):
    def __init__(self, url, file):
        Mobile.__init__(self, url, file)

    def scrap(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml')
        nums = soup.find('div', class_='pg-w -pvxl')
        links = nums.find_all('a', class_='pg')
        for link in links:
            if link.text.isdigit():
                index = int(link.text)
            else:
                index = None
            if index != None:
                self.url = self.url[0:len(self.url)-1]
                self.url = self.url+link.text
                super(List_Mobile, self).scrap()


def main():
    file = realmeFile
    realUrl = base_url + 'realme/'
    real_me = Mobile(realUrl, file)
    real_me.scrap()
    count = 0
    file = samsungFile
    sumsungUrl = base_url + 'samsung/?page=1'
    samsung = List_Mobile(sumsungUrl, file)
    samsung.scrap()
    count = 0
    file = huaweiFile
    huaweiUrl = base_url + 'huawei/?page=1'
    huawei = List_Mobile(huaweiUrl, file)
    huawei.scrap()
    count = 0
    file = xiaomiFile
    xiaomiUrl = base_url + 'xiaomi/?page=1'
    xiaomi = List_Mobile(xiaomiUrl, file)
    xiaomi.scrap()


main()
