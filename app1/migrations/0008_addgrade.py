# Generated by Django 4.2.7 on 2024-02-04 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_markattendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='addgrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.studentreg')),
            ],
        ),
    ]
