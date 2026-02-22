import logging
from datetime import datetime
import os
from scraper import scrape_trademark_announcements
from excel_generator import ExcelGenerator
from scheduler import job
import schedule
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    """Main function to run the scraper"""
    logger.info('IPM Scraper started')
    
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists('output'):
            os.makedirs('output')
        
        # Scrape data
        logger.info('Starting to scrape trademark announcements...')
        data = scrape_trademark_announcements()
        
        if data:
            # Generate Excel file
            logger.info(f'Found {len(data)} announcements')
            excel_gen = ExcelGenerator(data)
            output_file = excel_gen.generate_excel()
            logger.info(f'Excel file created: {output_file}')
        else:
            logger.warning('No data found to scrape')
    
    except Exception as e:
        logger.error(f'Error in main: {str(e)}')

def schedule_daily_task():
    """Schedule the scraper to run daily at 8:00 AM"""
    schedule.every().day.at("08:00").do(main)
    
    logger.info('Scheduler started - scraper will run daily at 08:00')
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--schedule':
        # Run with scheduler
        schedule_daily_task()
    else:
        # Run once
        main()
