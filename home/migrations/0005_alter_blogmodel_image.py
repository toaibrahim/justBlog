# Generated by Django 4.0.3 on 2022-03-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_blogmodel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(blank=True, default='/static/img/post1.jpg', null=True, upload_to='media'),
        ),
    ]
