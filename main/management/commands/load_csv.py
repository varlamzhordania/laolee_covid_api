import csv
from django.core.management.base import BaseCommand
from main.models import CovidCase
from django.conf import settings
from datetime import datetime


class Command(BaseCommand):
    help = 'Load data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            # Read the first row separately to get the header
            header = file.readline().strip()

            # Split the header using the appropriate delimiter (',' in this case)
            header_fields = header.split(',')

            # Use the split header as the fieldnames parameter
            reader = csv.DictReader(file, fieldnames=header_fields)

            # Skip the first row as it's already used as field names
            next(reader, None)

            for row in reader:
                # Convert date format from 'MM/DD/YYYY' to 'YYYY-MM-DD'
                date_of_confirmation = datetime.strptime(row['date_of_confirmation'], '%m/%d/%Y').strftime('%Y-%m-%d')
                # Check if 'date_of_discharge' is not a dash before parsing
                date_of_discharge = (
                    datetime.strptime(row['date_of_discharge'], '%m/%d/%Y').strftime('%Y-%m-%d')
                    if row['date_of_discharge'] != '-'
                    else None
                )
                # Modify the following lines based on your model fields
                CovidCase.objects.update_or_create(
                    case_id=row['case_id'],
                    age=row['age'],
                    gender=row['gender'],
                    nationality=row['nationality'],
                    imported_local=row['imported_local'],
                    place=row['place'],
                    public_healthcare_institution=row['public_healthcare_institution'],
                    status=row['status'],
                    date_of_confirmation=date_of_confirmation,
                    date_of_discharge=date_of_discharge,
                    places_visited=row['places_visited'],
                    residing_location=row['residing_location'],
                    residing_postal_code=row['residing_postal_code'],
                    reference_url=row['reference_url']
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
