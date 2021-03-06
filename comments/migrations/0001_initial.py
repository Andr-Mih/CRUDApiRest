# Generated by Django 4.0.3 on 2022-03-26 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_titile', models.CharField(max_length=100)),
                ('new_link', models.URLField()),
                ('new_creation_date', models.DateField()),
                ('new_author_name', models.CharField(max_length=30)),
                ('new_votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment_title', models.CharField(max_length=300)),
                ('coment_creation_date', models.DateField()),
                ('coment_author', models.CharField(max_length=40)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.news')),
            ],
        ),
    ]
