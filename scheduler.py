import schedule
import time
from scraper import scraper_function  # Replace with your actual scraper function import

def job():
    scraper_function()  # Call your scraper function here

# Schedule the job to run daily at 8:00 AM
schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)