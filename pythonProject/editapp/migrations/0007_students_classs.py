# Generated by Django 4.0 on 2021-12-22 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editapp', '0006_library_remove_teacher_stud_remove_teacher_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('add', models.TextField()),
                ('marks', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='classs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editapp.students')),
            ],
        ),
    ]
