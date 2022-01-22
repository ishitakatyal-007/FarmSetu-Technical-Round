import os
import csv

home_dir = os.getcwd()
data_dir = os.path.join(home_dir, 'dataset')
csv_headers = ['year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','win','spr','sum','aut','ann']

class DataToCSV:
    @classmethod
    def all_to_csv(cls):
        try:
            os.makedirs(os.path.join(data_dir, 'csv_files'))
        except OSError:
            print('Folder already exists..')
        for criterion_file in os.listdir(os.path.join(data_dir, 'date')):
            file_name = criterion_file.split('--')
            cls.to_csv(file_name[0], file_name[1])

    @classmethod                        
    def to_csv(cls, region, category, criterion='date'):
        file = region + "--" + category + "--" + criterion + ".txt"
        txt_contents = ''
        with open(os.path.join(os.path.join(data_dir, criterion), file), 'r') as txt_file:
            txt_contents = txt_file.read()    
        txt_file.close()

        txt_parsed = 'year' + txt_contents.split('year')[1]
        csv_file = file.replace('txt','csv')
        csv_directory = os.path.join(data_dir, 'csv_files')
        try:
            os.makedirs(csv_directory)
        except OSError:
            pass
        with open(os.path.join(csv_directory, csv_file), 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            txt_csv = [i for i in txt_parsed.split('\n')]
            all_recs = []
            for i in txt_csv:
                l = [m for m in i.split('  ')]
                record = {}
                for j, k in zip(l, csv_headers):
                    record[k] = j
                all_recs.append(record)
            # print(all_recs)
            writer.writerows(all_recs)

        csv_file.close()