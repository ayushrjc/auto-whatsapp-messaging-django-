# Generated by Django 3.0.8 on 2020-07-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('payment', models.CharField(max_length=122)),
                ('text', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
