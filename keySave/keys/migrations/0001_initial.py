# Generated by Django 2.1.7 on 2021-10-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allkeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginid', models.IntegerField(blank=True, null=True)),
                ('passwdencry', models.CharField(blank=True, db_column='passwdEncry', max_length=255, null=True)),
                ('siteName', models.CharField(blank=True, max_length=255, null=True)),
                ('key', models.CharField(blank=True, max_length=255, null=True)),
                ('algor', models.CharField(blank=True, max_length=255, null=True)),
                ('siteUrl', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'allKeys',
                'managed': False,
            },
        ),
    ]
