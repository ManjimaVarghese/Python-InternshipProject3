# Generated by Django 4.2.7 on 2024-02-22 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_uploadmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffapplyleave',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.studentreg'),
        ),
    ]