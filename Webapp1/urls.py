"""Webapp1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")

# @register_job(scheduler, "interval", seconds=3, id='test_job',replace_existing=True)
# def test_job():
#     print("a")
#     options = Options()
#     PATH = "/home/nguyen/Downloads/chromedriver"
#     order_number=1
#     with webdriver.Chrome(PATH, chrome_options= options) as driver:
#         driver.get("https://shopee.vn/")
#         time.sleep(2)
#         close_popup_button = driver.find_element_by_class_name("shopee-popup__close-btn") 
        
#         close_popup_button.click()
#         time.sleep(2)
#         driver.execute_script("window.scrollTo(0, 1000)") 
#         time.sleep(2)
#         driver.execute_script("window.scrollTo(0, 1000)") 
#         time.sleep(2)

#         categories = driver.find_elements_by_css_selector("a.home-category-list__category-grid")
#         category_urls = [category.get_attribute("href") for category in categories]

#         for url in category_urls:
#             for i in range(1):
#                 driver.get(url + f"?page={i}")
#                 print(url + f"?page={i}")
#                 time.sleep(2)
#                 driver.execute_script("window.scrollTo(0, 1000)") 
#                 time.sleep(2)
#                 driver.execute_script("window.scrollTo(0, 1000)") 
#                 time.sleep(2)
#                 driver.execute_script("window.scrollTo(0, 1000)") 
#                 time.sleep(2)
#                 driver.execute_script("window.scrollTo(0, 1000)") 
#                 time.sleep(2)
#                 driver.execute_script("window.scrollTo(0, 1000)") 
#                 time.sleep(2)
                
#                 products = driver.find_elements_by_css_selector("a[data-sqe='link']")
#                 product_links = [product.get_attribute("href") for product in products]
#                 for link in product_links:
#                     driver.get(link)
#                     driver.execute_script("window.scrollTo(0, 1000)")
#                     time.sleep(2)

#                     data = {    
#                         "STT":order_number,
#                         "title":driver.find_element_by_css_selector("div.attM6y>span").text,
#                         "price":driver.find_element_by_css_selector("div.Ybrg9j").text,
#                         "store":driver.find_element_by_css_selector("div._3uf2ae").text

#                     }
            
#                     with open("shopee.csv", "a", encoding='utf-8') as f:
#                         f.write(f"{data['STT']};{data['title']};{data['price']};{data['store']}\n")
#                     order_number += 1
# per-execution monitoring, call register_events on your scheduler
# register_events(scheduler)
# scheduler.start()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome),
    path('form',views.form),
    path('show', views.show),
    path('search', views.search),
    path('export-excel', views.export_excel, name='export_excel'),
    path('export-csv', views.export_csv, name='export_csv'),
]