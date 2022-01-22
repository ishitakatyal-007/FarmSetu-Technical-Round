import time
from django.core.management.base import BaseCommand

from ..utils.data_parser import DataToCSV

class Command(BaseCommand):
    help = 'Convert text files to CSV format'

    def add_arguments(self, parser):
        parser.add_argument(
            '--region', 
            type=str,
            default = 'all',
        )

        parser.add_argument(
            '--category', 
            type=str,
            default = 'all',
        )

        parser.add_argument(
            '--criterion', 
            type=str,
            default = 'date',
        )

    def handle(self, *args, **kwargs):
        self.stdout.write('CSV conversion initiated')
        region = ''
        if kwargs['region']:
            region += kwargs['region']
        category = ''
        if kwargs['category']:
            category += kwargs['category']
        criterion = ''
        if kwargs['criterion']:
            criterion += kwargs['criterion']
        
        data_to_csv = DataToCSV()
        if region == 'all' and category == 'all':
            data_to_csv.all_to_csv()
        else:
            data_to_csv.to_csv(region, category, criterion)

        self.stdout.write('CSV converted')
        time.sleep(5)
