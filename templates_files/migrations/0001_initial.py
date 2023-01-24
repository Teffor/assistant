# Generated by Django 4.1.4 on 2023-01-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='Таблицы')),
                ('photo1', models.ImageField(upload_to='media/', verbose_name='Первый график сравнения')),
                ('photo2', models.ImageField(upload_to='media/', verbose_name='Второй график сравнения')),
            ],
        ),
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='Таблицы')),
                ('first_title', models.CharField(blank=True, max_length=50, verbose_name='Заголовок для первого фото')),
                ('photo1', models.ImageField(upload_to='media/', verbose_name='Первое фото')),
                ('second_title', models.CharField(blank=True, max_length=50, verbose_name='Заголовок для второго фото')),
                ('photo2', models.ImageField(upload_to='media/', verbose_name='Второй график')),
            ],
        ),
        migrations.CreateModel(
            name='LastVacancyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='Описание профессии')),
                ('photo', models.ImageField(upload_to='media/', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=25, verbose_name='Название профессии')),
                ('logo_field', models.ImageField(upload_to='media/', verbose_name='Логотип')),
                ('title2', models.TextField(max_length=25, verbose_name='Название профессии в меню')),
                ('first_menu', models.TextField(max_length=25, verbose_name='Первый пункт меню')),
                ('second_menu', models.TextField(max_length=25, verbose_name='Второй пункт меню')),
                ('thierd_menu', models.TextField(max_length=25, verbose_name='Третий пункт меню')),
                ('fourth_menu', models.TextField(max_length=25, verbose_name='Четвертый пункт меню')),
                ('fifth_menu', models.TextField(max_length=25, verbose_name='Пятый пункт меню')),
                ('author', models.TextField(max_length=50, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_title', models.CharField(blank=True, max_length=50, verbose_name='Заголовок для таблицы')),
                ('content', models.TextField(blank=True, verbose_name='Таблица')),
                ('graph', models.ImageField(upload_to='media/', verbose_name='График')),
            ],
        ),
    ]
