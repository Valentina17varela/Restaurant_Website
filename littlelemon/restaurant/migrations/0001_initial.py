# Generated by Django 4.2.9 on 2024-01-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('identification_number', models.PositiveIntegerField()),
                ('phone_number', models.PositiveIntegerField()),
                ('guests', models.PositiveIntegerField()),
                ('reservation_date', models.CharField(max_length=50)),
                ('reservation_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=6)),
                ('description', models.CharField(max_length=250)),
                ('images', models.ImageField(upload_to='restaurant/static/images')),
                ('image_path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recomendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
