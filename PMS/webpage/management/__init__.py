from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from telebot import TeleBot


class Command(BaseCommand):
    help = 'deletes expired events'

    def handle(self, *args, **options):

        today = datetime.datetime.now()
        events = Event.objects.filter(date=datetime.date(2011,11,11))

        for e in events:
            e.delete()

        self.stdout.write('Expired events successfully deleted.')
