import time
from django.core.management.base import BaseCommand

from ..utils.web_scraper import WebScraper

class Command(BaseCommand):
    help = 'Updates DataBase'
  
    def handle(self, *args, **kwargs):
        self.stdout.write('Web-scraping initiated')
        web_scraper = WebScraper()
        web_scraper.scrape_web()
        self.stdout.write('Website scraped')
        time.sleep(5)
