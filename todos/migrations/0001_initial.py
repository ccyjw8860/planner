# Generated by Django 2.2.5 on 2021-02-09 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo', to='rooms.Room')),
            ],
        ),
        migrations.CreateModel(
            name='TodoPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('file', models.ImageField(upload_to='todo_photos')),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_photos', to='todos.Todo')),
            ],
        ),
    ]
