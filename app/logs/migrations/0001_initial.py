# Generated by Django 3.1.7 on 2021-03-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('put', 'Put'), ('delete', 'Delete'), ('get', 'Get'), ('post', 'Post')], max_length=10, verbose_name='Method Type')),
                ('ms', models.PositiveSmallIntegerField(verbose_name='Request MS')),
                ('timestamp', models.CharField(max_length=30, verbose_name='Timestamp')),
            ],
            options={
                'verbose_name': 'Logs',
                'verbose_name_plural': 'Logs',
            },
        ),
    ]
