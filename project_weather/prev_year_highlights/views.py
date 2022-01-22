import os
import csv
from django.shortcuts import render, redirect
from categories.models import CategoryModel

from regions.models import RegionModel

from .models import YearlyStatisticsModel

# Create your views here.
def update_stats(request):
    if request.method == 'POST':
        special_regions = ['England NW and N Wales', 'England SW and S Wales', 'England SE and Central S',]
        special_signs = ['', '\b', '\n', "", " ", ' ', '\t', None, '--', ' ---']
        data_dir = os.path.join(os.getcwd(), 'dataset\\csv_files')
        for files in os.listdir(data_dir):
            file_address = os.path.join(data_dir, files)
            with open(file_address, 'r') as csv_file:
                stats = csv.reader(csv_file)
                count_rec= 0
                for stat in stats:
                    if count_rec != 0:
                        year = int(stat[0])
                        region_parsed = files.split('--')[0].replace('_', ' ')
                        region = ''
                        if region_parsed == 'England and Wales' or region_parsed == 'England E and NE':
                            x = region_parsed.split(' and ')
                            region += x[0] + ' & ' + x[1]
                        elif region_parsed in special_regions:
                            x = region_parsed.split(' and ')
                            if region_parsed == 'England SE and Central S':
                                y = x[1]
                            else:
                                y = x[1].split(' ')[1] + ' ' + x[1].split(' ')[0]
                            region += x[0] + '/' + y
                        else:
                            region += region_parsed
                        category = files.split('--')[1]
                        print(year, region, category, stat[-1], type(stat[-1]))
                        stats_obj = YearlyStatisticsModel.objects.filter(
                            year=year, 
                            region=RegionModel.objects.filter(region_name=region).first(),
                            category=CategoryModel.objects.filter(category_alias=category).first(),
                            )
                        if stats_obj:
                            if stat[-1] in special_signs:
                                stats_obj.highlight_stats = -1
                            else:
                                stats_obj.highlight_stats = stat[-1]
                            stats_obj.update()
                        else:
                            new_obj = YearlyStatisticsModel.objects.create(
                                year=year, 
                                region=RegionModel.objects.filter(region_name=region).first(),
                                category=CategoryModel.objects.filter(category_alias=category).first(),
                            )
                            if stat[-1] in special_signs:
                                new_obj.highlight_stats = -1
                            else:
                                new_obj.highlight_stats = stat[-1]
                            new_obj.save()
                                                
                    count_rec += 1

        return redirect('/')

