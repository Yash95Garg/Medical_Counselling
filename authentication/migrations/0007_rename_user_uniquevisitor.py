# Generated by Django 4.0.5 on 2022-07-06 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_user_remove_postviews_post_delete_post_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='uniqueVisitor',
        ),
    ]
