from django.core.management.base import BaseCommand, CommandError
from tracker.models import Squirrel
import csv
import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file'], 'w') as fp:
            header = ['Y', 'X', 'Unique Squirrel ID', 'Shift', 'Date', 'Age', 'Primary Fur Color', 'Location', 'Specific Location', 'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other Activities', 'Kuks', 'Quaas', 'Moans', 'Tail flags',	'Tail twitches', 'Approaches', 'Indifferent', 'Runs from']
            field_names = [f.name for f in Squirrel._meta.fields]
            writer = csv.writer(fp)
            writer.writerow(header)
            for s in Squirrel.objects.all():
                s.date = s.date.strftime('%m%d%Y')
                writer.writerow([getattr(s, f) for f in field_names])
