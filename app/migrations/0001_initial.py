# Generated by Django 4.2.6 on 2024-01-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=100)),
                ('sprincipal', models.CharField(max_length=100)),
                ('sid', models.IntegerField()),
            ],
        ),
    ]
