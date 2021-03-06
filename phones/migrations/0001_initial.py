# Generated by Django 4.0.1 on 2022-01-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('image', models.ImageField(upload_to='', verbose_name='изображение')),
                ('release_date', models.DateField(verbose_name='дата релиза')),
                ('lte_exists', models.BooleanField(verbose_name='LTE')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='SLUG')),
            ],
            options={
                'verbose_name': 'телефон',
                'verbose_name_plural': 'телефоны',
            },
        ),
    ]
