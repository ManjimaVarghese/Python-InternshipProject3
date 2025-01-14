# Generated by Django 4.2.7 on 2024-02-11 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_staffreg_user_studentreg_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='replaystudleav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.studentreg')),
            ],
        ),
        migrations.CreateModel(
            name='replaystaffleav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=20)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.staffreg')),
            ],
        ),
    ]
