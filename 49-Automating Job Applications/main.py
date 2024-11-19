import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By for locating elements
import os
from dotenv import load_dotenv

load_dotenv()

LOGIN_URL = "https://www.linkedin.com/login"
JOBS_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords=python%20developer&location=Banglore%2C%20India"

def login():
    """Accepts cookies and logs in to the site."""
    driver.get(url=LOGIN_URL)
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys(os.getenv("EMAIL"))
    driver.find_element(By.ID, "password").send_keys(os.getenv("PASSWORD"))
    driver.find_element(By.ID, "password").submit()

def get_job_urls():
    """Looks up the available jobs and returns a LIST of urls with the first few matches."""
    driver.get(url=JOBS_URL)
    time.sleep(2)
    jobs = driver.find_elements(By.CLASS_NAME, "job-card-container__link")
    job_url_list = []
    for job in jobs:
        job_url = job.get_attribute("href")
        if job_url.find("www.linkedin.com/jobs/view/") >= 0 and job_url not in job_url_list:
            job_url_list.append(job_url)
    return job_url_list

def apply_to_job(link):
    """Takes a job listing url as a STR and submits an application if one-step apply is possible."""
    driver.get(url=link)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "jobs-apply-button").click()
    time.sleep(1)
    button = driver.find_element(By.CSS_SELECTOR, "footer button")
    print(button.text)
    if button.text == "Submit application":
        driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        print(f"*** Pretending to click on the \"{button.text}\" button. ***")
    else:
        print(f"One-step application is not possible for this job.")

driver = webdriver.Chrome()
login()
time.sleep(3)
url_list = get_job_urls()
if len(url_list) == 0:
    print("No jobs found.\nMake sure you're logged in properly or tweak the position or location name.")

for url in url_list:
    apply_to_job(url)
    time.sleep(5)

driver.close()
