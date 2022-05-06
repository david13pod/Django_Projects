# Generated by Django 3.0 on 2022-04-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('admission_number', models.IntegerField(unique=True)),
                ('is_qualified', models.BooleanField(default=False)),
                ('average_score', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('student_capacity', models.IntegerField()),
                ('students', models.ManyToManyField(to='testapis.Student')),
            ],
        ),
    ]