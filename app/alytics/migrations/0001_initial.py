# Generated by Django 3.2.4 on 2021-06-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraphFunc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('graphic', models.ImageField(upload_to='')),
                ('func_exception', models.TextField(blank=True, editable=False, null=True)),
                ('interval', models.IntegerField()),
                ('dt', models.IntegerField()),
                ('create_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]