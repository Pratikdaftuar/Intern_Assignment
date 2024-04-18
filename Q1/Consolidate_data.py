#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:





# In[274]:


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
    
    # Set up Chrome options for downloading files
    chrome_options = webdriver.ChromeOptions()
    download_dir = os.path.join(os.getcwd(), "prati")  # Define the directory for downloading files
    os.makedirs(download_dir, exist_ok=True)  # Create the download directory if it doesn't exist
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,  # Set the default download directory
        "download.prompt_for_download": False,  # Disable download prompts
        "download.directory_upgrade": True,  # Allow directory upgrades
        "safebrowsing.enabled": True  # Enable safe browsing
    })
    
    # Initialize Chrome webdriver with configured options
    driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    driver.get(base_url)

    # Click on the "MacroNutrient" button
    go_button = driver.find_element(By.XPATH, "//button[contains(text(), 'MacroNutrient')]")
    go_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'State-wise')]")))
    
    # Click on the "District" button
    o_button = driver.find_element(By.XPATH, "//button[contains(text(), 'District')]")
    o_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'ANDAMAN')]")))

    # Click on the "Export to CSV" button
    o_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Export to CSV')]")
    o_button.click()

    # Open the state dropdown menu
    o_button = driver.find_element(By.CLASS_NAME, "state_dropdown")
    o_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(), 'ANDHRA')]")))
    
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
    
    # Close the webdriver
    driver.quit()

# Run the scraping function
if __name__ == "__main__":
    scrape_data()


# In[284]:


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
    chrome_options = webdriver.ChromeOptions()

    # Set up download directory
    download_dir = os.path.join(os.getcwd(), "prati")
    os.makedirs(download_dir, exist_ok=True)
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
    
    # Loop through each list element to download individual files
    for i in range(1, 37):
        list_elements = driver.find_elements(By.XPATH, "//*[@role='option']")
        o_button = driver.find_element(By.XPATH, f"//li[contains(text(), '{list_elements[i].text}')]")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{list_elements[i].text}')]")))
        o_button.click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'District')]")))
        
        # Click on the "Export to CSV" button
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
    
    # Combine CSV files in each subdirectory
    for i in range(1, 37):
        sub_dir = list_elements[i].text
        download_dir = os.path.join(os.getcwd(), "prati")
        sub_dir_path = os.path.join(download_dir, sub_dir)
        os.makedirs(sub_dir_path, exist_ok=True)
        df1 = pd.read_csv(os.path.join(sub_dir_path, f"my-file ({i}).csv"))
        df2 = pd.read_csv(os.path.join(sub_dir_path, f"my-file ({i+36}).csv"))
        combined_df = pd.concat([df1, df2], ignore_index=True)
        combined_csv_path = os.path.join(sub_dir_path, "combined.csv")
        combined_df.to_csv(combined_csv_path, index=False)
    
    # Close the webdriver
    driver.quit()

# Run the scraping function
if __name__ == "__main__":
    scrape_data()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




