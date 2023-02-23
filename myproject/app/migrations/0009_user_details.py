# Generated by Django 4.1.7 on 2023-02-23 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_multiple_exam_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=25, null=True)),
                ('contact_no', models.CharField(max_length=25, null=True)),
                ('email', models.CharField(max_length=25, null=True)),
                ('pic', models.FileField(upload_to='user_pic')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL)),
                ('user_auth', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_details_auth_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
