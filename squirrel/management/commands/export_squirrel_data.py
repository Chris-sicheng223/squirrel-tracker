from django.core.management.base import BaseCommand
from squirrel.models import Sighting
import csv

class Command(BaseCommand):
    help = 'Export all data to csv file'
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'w', newline='') as csvfile:
            attributes = [
                    'latitude',
                    'longitude',
                    'unique_squirrel_id',
                    'shift',
                    'date',
                    'age',
                    'primary_fur_color',
                    'location',
                    'specific_location',
                    'running',
                    'chasing',
                    'climbing',
                    'eating',
                    'foraging',
                    'other_activities',
                    'kuks',
                    'quaas',
                    'moans',
                    'tail_flags',
                    'tail_twitches',
                    'approaches',
                    'indifferent',
                    'runs_from'
            ]
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(attributes)
            for row in Sighting.objects.all():
                writer.writerow([getattr(row, attribute) for attribute in attributes])
        msg=f'Exporting sighting data to {path}...Done!'
        self.stdout.write(self.style.SUCCESS(msg))
