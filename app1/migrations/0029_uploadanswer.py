# Generated by Django 4.2.7 on 2024-02-19 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_qpaperupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadanswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answersheet', models.ImageField(default='', upload_to='profile')),
            ],
        ),
    ]
