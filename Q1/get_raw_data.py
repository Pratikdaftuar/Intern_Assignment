#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import os
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import shutil

def scrape_data():
    # Define the base URL
    base_url = "https://soilhealth.dac.gov.in/piechart"
    
    # Set up Chrome options for download directory
    chrome_options = webdriver.ChromeOptions()
    download_dir = os.path.join(os.getcwd(), "prati")
    os.makedirs(download_dir, exist_ok=True)
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    driver.get(base_url)

    # Click the "MacroNutrient" button
    go_button = driver.find_element(By.XPATH, "//button[contains(text(), 'MacroNutrient')]")
    go_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'State-wise')]")))
    
    # Click the "District" button
    o_button = driver.find_element(By.XPATH, "//button[contains(text(), 'District')]")
    o_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'ANDAMAN')]")))
    
    # Click the "Export to CSV" button
    o_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Export to CSV')]")
    o_button.click()

    # Click the "State" dropdown
    o_button = driver.find_element(By.CLASS_NAME, "state_dropdown")
    o_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'ANDHRA')]")))
    
    # Iterate through each state and download CSV
    list_elements = driver.find_elements(By.XPATH, "//*[@role='option']")
    for i in range(1,37):
        list_elements = driver.find_elements(By.XPATH, "//*[@role='option']")
        o_button = driver.find_element(By.XPATH, f"//li[contains(text(), '{list_elements[i].text}')]")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{list_elements[i].text}')]")))
        o_button.click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'District')]")))
        
        o_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Export to CSV')]")
        o_button.click()
        o_button = driver.find_element(By.CLASS_NAME, "state_dropdown")
        o_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'ANDHRA')]")))
    
    # Quit the WebDriver session
    driver.quit()

# Run the scraping function
if __name__ == "__main__":
    scrape_data()


# In[ ]:


import os
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import shutil
import pandas as pd

def scrape_data():
    # Define the base URL
    base_url = "https://soilhealth.dac.gov.in/piechart"
    # Configure Chrome options for download settings
    chrome_options = webdriver.ChromeOptions()
    download_dir = os.path.join(os.getcwd(), "prati")  # Define the directory where downloaded files will be saved
    os.makedirs(download_dir, exist_ok=True)  # Create the download directory if it doesn't exist
    # Set Chrome options for download behavior
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    
    # Initialize Chrome webdriver with configured options
    driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    driver.get(base_url)

    # Click on the "MicroNutrient" button
    go_button = driver.find_element(By.XPATH, "//button[contains(text(), 'MicroNutrient')]")
    go_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'State-wise')]")))
    
    # Click on the "District" button
    o_button = driver.find_element(By.XPATH, "//button[contains(text(), 'District')]")
    o_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'ANDAMAN')]")))

    # Open the state dropdown menu
    o_button = driver.find_element(By.CLASS_NAME, "state_dropdown")
    o_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'ANDHRA')]")))
    
    list_elements = driver.find_elements(By.XPATH, "//*[@role='option']")
    
    # Loop through each list element to download files
    for i in range(1, 37):
        list_elements = driver.find_elements(By.XPATH, "//*[@role='option']")
        o_button = driver.find_element(By.XPATH, f"//li[contains(text(), '{list_elements[i].text}')]")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{list_elements[i].text}')]")))
        o_button.click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'District')]")))
        
        o_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Export to CSV')]")
        o_button.click()
        o_button = driver.find_element(By.CLASS_NAME, "state_dropdown")
        o_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'ANDHRA')]")))
            # Move downloaded files to subdirectories
    for i in range(1, 73):
        if(i % 36) != 0:
            sub_dir = list_elements[i % 36].text
        else:
            sub_dir = list_elements[36].text
        sub_dir_path = os.path.join(download_dir, sub_dir)
        os.makedirs(sub_dir_path, exist_ok=True)
    
        source_file = f"C:\\Users\\HP\\Desktop\\Python projects\\Untitled Folder\\prati\\my-file ({i}).csv"

        shutil.move(source_file, sub_dir_path)
    
    # Quit the webdriver
    driver.quit()

# Run the scraping function
if __name__ == "__main__":
    scrape_data()

