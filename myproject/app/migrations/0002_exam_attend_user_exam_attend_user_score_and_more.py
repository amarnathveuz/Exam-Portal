# Generated by Django 4.1.7 on 2023-03-06 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_attend_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('login_user', 'login_user'), ('non_login_user', 'non_login_user')], max_length=25, null=True)),
                ('created_dt', models.DateField(auto_now_add=True)),
                ('created_tm', models.TimeField(auto_now_add=True)),
                ('auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Exam_attend_user_auth_id', to=settings.AUTH_USER_MODEL)),
                ('exam_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Exam_attend_user_exam_id', to='app.main_exam_master')),
            ],
        ),
        migrations.CreateModel(
            name='exam_attend_user_score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mark', models.IntegerField(null=True)),
                ('attend_status', models.BooleanField(default=False)),
                ('Question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_attend_user_score_Question_Bank_id', to='app.main_question_bank')),
                ('correct_answer', models.ManyToManyField(related_name='exam_attend_user_score_Question_Bank_id', to='app.question_bank_multiple_choice')),
                ('exam_attend_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_attend_user_score_user_id', to='app.exam_attend_user')),
                ('section_question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_attend_user_score_question_id', to='app.section_question_mapping')),
            ],
        ),
        migrations.CreateModel(
            name='exam_attend_user_initial_field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=25, null=True)),
                ('Exam_inital_field_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_attend_user_initial_field_id_Exam_inital_field', to='app.exam_inital_field')),
                ('exam_attend_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_attend_user_initial_field_attend_id', to='app.exam_attend_user')),
            ],
        ),
    ]