from django.core.management.base import BaseCommand
from api.models import Survey
import pandas as pd

class Command(BaseCommand):
    help = "Export survey data to CSV"

    def handle(self, *args, **kwargs):
        surveys = Survey.objects.all().values()
        if not surveys:
            self.stdout.write(self.style.WARNING("No survey data found."))
            return

        df = pd.DataFrame(surveys)
        df.to_csv("survey_data.csv", index=False)
        self.stdout.write(self.style.SUCCESS("Survey data exported to survey_data.csv"))
