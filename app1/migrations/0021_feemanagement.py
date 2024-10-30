# Generated by Django 4.2.7 on 2024-02-15 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_companies_placementcontact_replaying_for_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='feemanagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default='')),
                ('fees', models.IntegerField(default='')),
                ('department_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app1.department')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.studentreg')),
            ],
        ),
    ]