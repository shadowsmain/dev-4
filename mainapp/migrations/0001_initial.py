# Generated by Django 2.2 on 2021-05-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.TextField(verbose_name='Число')),
            ],
            options={
                'verbose_name': 'Число',
                'verbose_name_plural': 'Числа',
            },
        ),
    ]
