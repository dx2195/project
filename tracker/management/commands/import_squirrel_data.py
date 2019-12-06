from django.core.management.base import BaseCommand, CommandError
from tracker.models import Squirrel
import csv
import datetime as dt

class Command(BaseCommand):
    help = 'Import 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            item['Date'] = datetime.datetime.strptime(item['Date'],'%m%d%Y')
            s = Squirrel()
            try:
                s.latitude = item['Y']
                s.longitude = item['X']
                s.unique_squirrel_ID = item['Unique Squirrel ID']
                s.shift = item['Shift']
                s.date = item['Date']
                s.age = item['Age']
                s.primary_fur_color = item['Primary Fur Color']
                s.location = item['Location']
                s.specific_location = item['Specific Location']
                s.running = item['Running']
                s.chasing = item['Chasing']
                s.climbing = item['Climbing']
                s.eating = item['Eating']
                s.foraging = item['Foraging']
                s.other_activities = item['Other Activities']
                s.kuks = item['Kuks']
                s.quaas = item['Quaas']
                s.moans = item['Moans']
                s.tail_flags = item['Tail flags']
                s.tail_twitches = item['Tail twitches']
                s.approaches = item['Approaches']
                s.indifferent = item['Indifferent']
                s.runs_from = item['Runs from']
            except:
                pass
            s.save()

