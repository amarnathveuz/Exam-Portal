# Generated by Django 4.1.7 on 2023-02-24 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_user_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_general_instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('instruction', models.TextField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('exam_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Exam_general_instruction_exam_id', to='app.exam_master')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]