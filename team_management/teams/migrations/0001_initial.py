# Generated by Django 4.1.6 on 2023-02-12 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('role', models.CharField(choices=[('R', "Regular - Can't delete members"), ('A', 'Admin - Can delete members')], default='R', max_length=1)),
            ],
        ),
    ]
