# Generated by Django 3.2.7 on 2022-01-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='additionaldata',
            name='user_app_ad_email_096196_idx',
        ),
        migrations.AlterField(
            model_name='additionaldata',
            name='email',
            field=models.EmailField(db_index=True, max_length=254),
        ),
    ]
