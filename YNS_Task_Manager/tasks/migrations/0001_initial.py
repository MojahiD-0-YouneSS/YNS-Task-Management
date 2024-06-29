# Generated by Django 4.2.13 on 2024-06-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('priority_level', models.CharField(choices=[('alpha', 'Important'), ('beta', 'Somewhat Important'), ('omega', 'Less Important')], max_length=10)),
                ('completion_status', models.BooleanField(default=False)),
            ],
        ),
    ]
