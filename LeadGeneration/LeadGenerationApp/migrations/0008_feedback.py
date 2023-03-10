# Generated by Django 4.1.3 on 2023-03-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGenerationApp', '0007_administrator'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionid', models.CharField(default='', max_length=15)),
                ('customerid', models.CharField(default='', max_length=15)),
                ('customername', models.CharField(default='', max_length=15)),
                ('callerid', models.CharField(default='', max_length=15)),
                ('status', models.CharField(default='', max_length=15)),
                ('callername', models.CharField(default='', max_length=15)),
                ('currentdate', models.DateField(default='', max_length=15)),
                ('phonestatus', models.CharField(default='', max_length=15)),
                ('conversation', models.CharField(default='', max_length=100)),
                ('leadstatus', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
