# Generated by Django 4.0.2 on 2023-03-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('monday', models.IntegerField(default=0)),
                ('tuesday', models.IntegerField(default=0)),
                ('wednesday', models.IntegerField(default=0)),
                ('thursday', models.IntegerField(default=0)),
                ('friday', models.IntegerField(default=0)),
                ('saturday', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='adminlogindetails',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
