# Generated by Django 4.2 on 2023-04-08 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_todo_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitems',
            name='createAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='todoitems',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todoitems',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todoitems',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='todoitems',
            name='todo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.todo'),
        ),
    ]
