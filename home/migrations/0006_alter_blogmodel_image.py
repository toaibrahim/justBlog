# Generated by Django 4.0.3 on 2022-03-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_blogmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(default='/static/img/post1.jpg', upload_to='media'),
        ),
    ]
