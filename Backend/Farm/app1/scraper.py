# from django.core.management.base import BaseCommand
# import pandas as pd
# from crop_predictor.models import CropPrice

# class Command(BaseCommand):
#     help = 'Import crop prices from CSV file'

#     def add_arguments(self, parser):
#         parser.add_argument('csv_file', type=str, help='Path to the CSV file')

#     def handle(self, *args, **options):
#         try:
#             data = pd.read_csv(options['csv_file'])
            
#             state_mapping = {
#                 'Andhra Pradesh': 'AP',
#                 'Telangana': 'TG',
#                 'Kerala': 'KL'
#             }
            
#             for _, row in data.iterrows():
#                 if row['State'] in state_mapping:
#                     CropPrice.objects.create(
#                         commodity=row['Commodity'],
#                         state=state_mapping[row['State']],
#                         modal_price=row['Modal_x0020_Price'],
#                         date=pd.to_datetime(row.get('Date', pd.Timestamp.now())).date()
#                     )
            
#             self.stdout.write(
#                 self.style.SUCCESS('Successfully imported crop prices')
#             )
            
#         except Exception as e:
#             self.stdout.write(
#                 self.style.ERROR(f'Error importing data: {str(e)}')
#             )