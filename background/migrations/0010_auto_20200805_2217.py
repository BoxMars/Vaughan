# Generated by Django 3.0.8 on 2020-08-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background', '0009_article_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='tag',
        ),
    ]
