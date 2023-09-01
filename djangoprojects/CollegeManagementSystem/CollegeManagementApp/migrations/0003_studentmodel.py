# Generated by Django 4.2.3 on 2023-08-31 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CollegeManagementApp', '0002_coursemodel_course_duration_coursemodel_course_fee'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('image', models.ImageField(upload_to='image/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollegeManagementApp.coursemodel')),
            ],
        ),
    ]