# Generated by Django 4.2.7 on 2024-02-15 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_allocatefee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocatestudent',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='allocatestudent',
            name='department',
        ),
        migrations.RemoveField(
            model_name='allocatestudent',
            name='student',
        ),
        migrations.RemoveField(
            model_name='contactplacement',
            name='student',
        ),
        migrations.RemoveField(
            model_name='replaying_for_contact',
            name='student',
        ),
        migrations.DeleteModel(
            name='allocatefee',
        ),
        migrations.DeleteModel(
            name='allocatestudent',
        ),
        migrations.DeleteModel(
            name='companies',
        ),
        migrations.DeleteModel(
            name='contactplacement',
        ),
        migrations.DeleteModel(
            name='replaying_for_contact',
        ),
    ]
