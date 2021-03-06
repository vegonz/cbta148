# Generated by Django 2.1.1 on 2018-10-01 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_property_propertyimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='administration.Property')),
            ],
        ),
    ]
