from django.core.management.base import BaseCommand
from calls.models import Call

class Command(BaseCommand):
    help = 'Prints a summary of all calls'

    def handle(self, *args, **kwargs):
        calls = Call.objects.all()
        with open('calls_summary.txt', 'w') as f:
            for call in calls:
                f.write(f'{call.name}, {call.email}, {call.message}, {call.timestamp}\n')
        self.stdout.write(self.style.SUCCESS('Summary saved to calls_summary.txt'))
