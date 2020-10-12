import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(filename='flight.log',format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%y/%m/%d %H:%M:%S', level=logging.INFO, filemode='w')


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#initialize Chrome Driver
driver=webdriver.Chrome(executable_path='C:/bin/chromedriver3', chrome_options=chrome_options)

#open the browser
driver.get('https://www.cleartrip.com/')
driver.maximize_window()
logging.info('ChromeDriver was opened successfully')


#round trip
round_trip=driver.find_element_by_id('RoundTrip')
round_trip.click()
time.sleep(2)


#Frankfurt
departure=driver.find_element_by_id('FromTag')
departure.click()
departure.send_keys('fra')
time.sleep(4)

cities_departure=driver.find_elements_by_xpath('//li[@class="list"]')
for city_1 in cities_departure:
    if 'FRA' in city_1.text:
        city_1.click()
        break
time.sleep(3)
logging.info('Frankfurt was selected')


#San Francisco
arrival=driver.find_element_by_id('ToTag')
arrival.click()
arrival.send_keys('san')
time.sleep(4)

cities_arrival=driver.find_elements_by_xpath('//li[@class="list"]')
for city_2 in cities_arrival:
    if 'SFO' in city_2.text:
        city_2.click()
        break
time.sleep(3)
logging.info('San Francisco was selected')

#departure date
departure_date=driver.find_element_by_xpath('//td[@data-month="9"]/a[text()="2"]')
departure_date.click()
time.sleep(2)

#next button
next=driver.find_element_by_xpath('//a[@class="nextMonth "]')
next.click()

#return date
return_date=driver.find_element_by_xpath('//td[@data-month="11"]/a[text()="21"]')
return_date.click()
time.sleep(2)

#adults
adults=driver.find_element_by_id('Adults')
dropdown_1=Select(adults)
dropdown_1.select_by_index(1)
time.sleep(2)

#children
children=driver.find_element_by_id('Childrens')
dropdown_2=Select(children)
dropdown_2.select_by_value('3')
time.sleep(2)
logging.info('2 adults and 3 children were selected')

#more options
more_options=driver.find_element_by_id('MoreOptionsLink')
more_options.click()
time.sleep(1)

#class of travel
class_of_travel=driver.find_element_by_id('Class')
dropdown_3=Select(class_of_travel)
dropdown_3.select_by_visible_text('Premium Economy')
time.sleep(2)
logging.info('Premium Economy Class was selected')

#search flights
search_flights=driver.find_element_by_id('SearchBtn')
search_flights.click()

#explicit wait
wait=WebDriverWait(driver,20)
non_stop_checkbox=wait.until(EC.element_to_be_clickable((By.XPATH, '//p[text()="Non-stop"]' )))
non_stop_checkbox.click()
time.sleep(2)

#change currency INR -> USD
currency=driver.find_element_by_xpath('//span[@class="fs-2 c-inherit"]')
currency.click()
time.sleep(2)

USD=driver.find_element_by_xpath('//span[text()="US Dollar"]')
USD.click()
time.sleep(2)

logging.info('We use the USD currency')

#select flight #1
first_flight=driver.find_element_by_xpath('//div[@class="col-19"]/div[2]/div[7]/div[1]/div[1]/div[2]/div[4]/button')
first_flight.click()

time.sleep(2)

#switch to child window
child_window=driver.window_handles[1]
driver.switch_to.window(child_window)
time.sleep(10)

#continue booking
continue_booking=driver.find_element_by_id('itineraryBtn')
continue_booking.location_once_scrolled_into_view
time.sleep(2)
continue_booking.click()
time.sleep(2)

#continue booking
continue_booking_2=driver.find_element_by_id('LoginContinueBtn_1')
continue_booking_2.click()
time.sleep(2)

#save screenshot
driver.save_screenshot('error_msg.png')
logging.info('Screenshot was captured')

#close driver
driver.close()
logging.info('The Driver was closed successfully')






















