from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):

    help = "Display current time"

    def add_arguments(self, parser):

        parser.add_argument("name",type=str,help="use to fetch username")

    def handle(self, *args, **kwargs):

        time = timezone.now().strftime("%X")

        self.stdout.write(f"{kwargs['name']} , it is {time}")