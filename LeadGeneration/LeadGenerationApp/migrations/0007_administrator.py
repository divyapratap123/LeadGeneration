# Generated by Django 4.1.3 on 2023-02-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGenerationApp', '0006_employee_password_employee_repassword_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileno', models.CharField(default='', max_length=45)),
                ('adminname', models.CharField(default='', max_length=45)),
                ('password', models.CharField(default='', max_length=45)),
            ],
        ),
    ]
