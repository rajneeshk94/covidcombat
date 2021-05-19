# Generated by Django 3.2.2 on 2021-05-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidcombatapp', '0003_examine'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, null=True, unique=True)),
                ('test_result', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative')], max_length=20, null=True)),
                ('oxygen_level', models.CharField(choices=[('Above 95', 'Above 95'), ('Below 95', 'Below 95')], max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='examine',
            name='Name',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]