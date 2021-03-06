# Generated by Django 3.0.5 on 2020-06-07 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200605_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Book')),
            ],
            options={
                'verbose_name': 'Book Image',
                'verbose_name_plural': 'Book Image',
            },
        ),
    ]
