# Generated by Django 4.2.6 on 2023-10-27 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.person')),
                ('employee_id', models.CharField(max_length=10)),
                ('hire_date', models.DateField()),
            ],
            bases=('myapp.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.person')),
                ('student_id', models.CharField(max_length=10)),
                ('enrollment_date', models.DateField()),
            ],
            bases=('myapp.person',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.person')),
                ('teacher_id', models.CharField(max_length=10)),
                ('hire_date', models.DateField()),
            ],
            bases=('myapp.person',),
        ),
    ]
