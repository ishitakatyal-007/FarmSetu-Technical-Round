import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from .db_update import DBUpdater

browser = webdriver.Chrome(ChromeDriverManager().install())
urls_list = ["https://www.metoffice.gov.uk/research/climate/maps-and-data/uk-and-regional-series#yearOrdered"]

home_folder = os.getcwd() 

class WebScraper:              
    regions = {}
    params = {}
    statistics = []

    @staticmethod
    def different_permutations_and_combinations(regions, parameters, statistics):
        for i in regions:
            for j in parameters:
                for k in statistics:
                    try:
                        data_folder = os.path.join(home_folder, 'dataset\\'+k)
                        os.makedirs(data_folder)
                    except OSError:
                        print('Folder already exists')
                    cur_url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/" + j + "/" + k + "/" + i + ".txt"
                    browser_1 = webdriver.Chrome(ChromeDriverManager().install())
                    browser_1.get(cur_url)
                    info_element = browser_1.find_element_by_tag_name('pre')
                    file_name = i + "--" + j + "--" + k + ".txt"
                    file_loc = os.path.join(data_folder, file_name)
                    with open(file_loc, 'w') as txt_file:
                        txt_file.write(info_element.text)
                    time.sleep(1)
                    browser_1.close()

    @classmethod
    def scrape_web(cls):
        for url in urls_list:
            browser.get(url)
            time.sleep(5)
            browser.find_element_by_id('ccc-recommended-settings').click()
            time.sleep(5)
            region_el = browser.find_element_by_id('region')
            for option in region_el.find_elements_by_tag_name('option'):
                region_val = option.get_attribute('value')
                if not option.text =="Choose a region":
                    cls.regions[region_val] = option.text
            params_el = browser.find_element_by_id('parameter')
            for option in params_el.find_elements_by_tag_name('option'):
                param_val = option.get_attribute('value')
                if not option.text == "Choose a parameter":
                    cls.params[param_val] = option.text
            statistic_el = browser.find_elements_by_tag_name('input')
            for option in statistic_el:
                stats_val = option.get_attribute('value')
                if stats_val != '':
                    cls.statistics.append(stats_val)

        print('Initiating Update on Regions')
        db_updater_regions = DBUpdater(cls.regions, 'Regions')
        db_updater_regions.__call__(cls.regions, 'Regions')
        print('Updated Regions')
        print('Initiating Update on Categories')
        db_updater_categories = DBUpdater(cls.params, 'Categories')
        db_updater_categories.__call__(cls.params, 'Categories')
        print('Updated Categories')
        print('Initiating Update on Criterion')
        db_updater_stats = DBUpdater(cls.statistics, 'Criterion')
        db_updater_stats.__call__(cls.statistics, 'Criterion')
        print('Updated Criterion')

        # cls.different_permutations_and_combinations(
        #         cls.regions, 
        #         cls.params, 
        #         cls.statistics
        #         )
        # browser.close()