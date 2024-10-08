# Generated by Django 5.1 on 2024-09-02 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('birth_date', models.DateField(max_length=12)),
                ('course_period', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='student_photos/')),
                ('courses', models.ManyToManyField(to='CadStudent.course')),
            ],
        ),
    ]
