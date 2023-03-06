# Generated by Django 4.1.7 on 2023-03-06 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_exam_attend_user_exam_attend_user_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_question_bank',
            name='question_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='main_question_bank',
            name='question_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='main_question_bank',
            name='question_hi',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='main_question_bank',
            name='question_ta',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='main_question_bank',
            name='question_ur',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question_bank_multiple_choice',
            name='choice_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question_bank_multiple_choice',
            name='choice_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question_bank_multiple_choice',
            name='choice_hi',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question_bank_multiple_choice',
            name='choice_ta',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question_bank_multiple_choice',
            name='choice_ur',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='main_question_bank',
            name='Question',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Main_exam_language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('language_access', models.CharField(choices=[('en', 'English'), ('ar', 'Arabic '), ('ur', 'Urdu'), ('ta', 'Tamil'), ('hi', 'Hindi')], max_length=25)),
                ('Exam_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Main_exam_language_eaxm_id', to='app.main_exam_master')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
