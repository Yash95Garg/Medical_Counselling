# Generated by Django 4.0.5 on 2022-06-30 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_contact_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='queryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
            ],
        ),
    ]