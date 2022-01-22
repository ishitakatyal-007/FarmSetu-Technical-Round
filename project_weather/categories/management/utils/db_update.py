from categories.models import CategoryModel
from criteria.models import CriterionModel
from regions.models import RegionModel

class DBUpdater:
    def __init__(self, variable_list_to_update, model_name:str):
        self.variable_list_to_update = variable_list_to_update
        self.model_name = model_name

    @staticmethod
    def parse_queryset_to_list(queryset, field_name):
        record_names_list = [] 
        for record in queryset:
            record_names_list.append(record[field_name])

        return record_names_list

    @classmethod
    def fetch_db_queryset(self, model_name:str) -> list:
        queryset = None
        if model_name == 'Regions':
            queryset = RegionModel.objects.values('region_name').all()
            queryset_list = self.parse_queryset_to_list(queryset, 'region_name')
        elif model_name == 'Categories':
            queryset = CategoryModel.objects.values('category_name').all()
            queryset_list = self.parse_queryset_to_list(queryset, 'category_name')
        elif model_name == 'Criterion':
            queryset = CriterionModel.objects.values('criterion_name').all()
            queryset_list = self.parse_queryset_to_list(queryset, 'criterion_name')
        else:
            print('There is no model with that name.. OOPS:(')    

        return queryset_list

    @classmethod
    def update_table(self, model, var, alias=None):
        if model == 'Regions':
            region_var = RegionModel(region_name=var)
            region_var.save()
        elif model == 'Categories':
            category_var = CategoryModel(category_name=var, category_alias=alias)
            category_var.save()
        elif model == 'Criterion':
            criterion_var = CriterionModel(criterion_name=var)
            criterion_var.save()
        
    @classmethod
    def delete_non_existent_recs(self, deleted_recs_list, model):
        if model == 'Regions':
            RegionModel.objects.filter(region_name__in=[deleted_recs_list]).delete()
        if model == 'Categories':
            CategoryModel.objects.filter(category_name__in=[deleted_recs_list]).delete()
        if model == 'Criterion':
            CriterionModel.objects.filter(criterion_name__in=[deleted_recs_list]).all().delete()

    @classmethod
    def parse_record_names(self, variable_list_to_update, model_name):       
        db_list = self.fetch_db_queryset(model_name=model_name)
        present_count = updated_count = deleted_count = 0
        if type(variable_list_to_update) == list:
            for var_name in variable_list_to_update:
                if var_name in db_list:
                    present_count += 1
                else:
                    self.update_table(model_name, var_name)
                    updated_count += 1

        if type(variable_list_to_update) == dict:
            for alias, name in variable_list_to_update.items():
                if name in db_list:
                    present_count += 1
                else:
                    self.update_table(model_name, name, alias)
                    updated_count += 1

        delete_records = []
        for rec_name in db_list:
            if rec_name not in variable_list_to_update:
                delete_records.append(rec_name)
        
        deleted_count += len(delete_records)
        self.delete_non_existent_recs(delete_records, model_name)
        print({model_name: 
            {'Records new created': updated_count,
            'Records matched': present_count,
            'Records deleted': deleted_count,
            }})
    
    def __call__(self, variable_list_to_update:list, model_name:str):
        self.parse_record_names(variable_list_to_update, model_name)