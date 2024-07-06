from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
import pandas as pd 
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse




def index(requests):
    if requests.method == 'GET':
        citys = ['Bengaluru']        
        return render(requests, 'mainapp/index.html', context={'city': citys})
    
    if requests.method == 'POST':
        city = requests.POST.get('city')
        area = requests.POST.get('area')
        area_ls = area.split(' ')
        area = '+'.join(area_ls)
        driver_path = 'mainapp/driver/msedgedriver.exe'

        service = Service(driver_path)
        driver = webdriver.Edge(service=service)
        address = f'https://www.google.com/search?q=list+of+it+companies+in+{area}+{city}'
        driver.get(address)
        driver.maximize_window()


        more_btn = driver.find_element(By.CLASS_NAME, 'S8ee5')
        more_btn.click()
        time.sleep(11)

        companies = driver.find_elements(By.CLASS_NAME, 'VkpGBb')
        websits = []
        phones = []
        comp_names = []
        df = pd.DataFrame(columns=['Company', 'Website', 'Phone no'])
        while len(companies) >0:
            for comp in companies:
                comp.click()
                time.sleep(11)
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                title = soup.find('h2', attrs={'class': 'qrShPb'})
                comp_names.append(title.text)
                links = soup.find_all('a', attrs={'class': 'n1obkb'})
                try:
                    websits.append(links[0].get('href'))
                except:
                    websits.append(' ')
                try:
                    phones.append(links[-1].get('data-phone-number'))
                except:
                    phones.append(' ')
            
            data = pd.DataFrame({'Company': comp_names, 'Website': websits, 'Phone no': phones})
            df = pd.concat([df, data], ignore_index=True) 
            df.to_csv('mainapp/static/companies.csv') 
            websits = []
            phones = []
            comp_names = [] 
            
            try:
                more_btn = driver.find_element(By.ID, 'pnnext')
                more_btn.click()
                time.sleep(11)
                companies = driver.find_elements(By.CLASS_NAME, 'VkpGBb')
            except:
                companies = []


        driver.quit()

        return HttpResponse(websits)