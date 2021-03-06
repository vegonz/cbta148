# Generated by Django 2.1.1 on 2018-10-04 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181004_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner_image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d/files'),
        ),
        migrations.AlterField(
            model_name='postfile',
            name='file',
            field=models.FileField(upload_to='posts/%Y/%m/%d/files'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(upload_to='posts/%Y/%m/%d/images/IMG_/%Y/%m/%d/%s'),
        ),
    ]
