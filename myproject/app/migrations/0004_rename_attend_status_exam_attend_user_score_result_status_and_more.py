# Generated by Django 4.1.7 on 2023-03-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_main_question_bank_question_ar_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam_attend_user_score',
            old_name='attend_status',
            new_name='result_status',
        ),
        migrations.AddField(
            model_name='exam_attend_user',
            name='attend_status',
            field=models.BooleanField(default=False),
        ),
    ]
