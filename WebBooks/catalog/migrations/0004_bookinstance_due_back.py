# Generated by Django 4.0.2 on 2022-04-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_bookinstance_due_back_bookinstance_borrower'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(blank=True, help_text='Введите конец срока статуса', null=True, verbose_name='Дата окончания статуса'),
        ),
    ]
