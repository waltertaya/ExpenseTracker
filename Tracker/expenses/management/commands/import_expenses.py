import pandas as pd
from django.core.management.base import BaseCommand
from expenses.models import Expense


class Command(BaseCommand):
    help = 'Import expenses from Excel sheet'

    def handle(self, *args, **options):
        import os

        file_path = os.path.join(os.path.dirname(__file__), 'Expenses.xlsx')
        print(f"Attempting to read file from: {file_path}")

        df = pd.read_excel(file_path)

        for index, row in df.iterrows():
            _, created = Expense.objects.get_or_create(
                id=row['id'],
                defaults={
                    'title': row['title'],
                    'subtitle': row['subtitle'],
                    'authors': row['authors'],
                    'publisher': row['publisher'],
                    'published_date': row['published_date'],
                    'category': row['category'],
                    'distribution_expense': row['distribution_expense'],
                }
            )

            if not created:
                print(f"Expense with id {row['id']} already exists.")

        self.stdout.write(self.style.SUCCESS('Successfully imported expenses'))
