# Generated by Django 2.1.15 on 2024-01-29 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_alter_expense_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='book_id',
            field=models.CharField(auto_created=True, default='0', editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.CharField(max_length=100),
        ),
    ]
