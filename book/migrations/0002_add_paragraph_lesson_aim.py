# Generated by Django 4.1.1 on 2022-12-20 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnumber', models.CharField(max_length=100, verbose_name='paragraph number')),
                ('paragraph', models.TextField(verbose_name='paragraph')),
                ('plname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.add_lesson', verbose_name='lesson name')),
            ],
        ),
        migrations.CreateModel(
            name='lesson_aim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laAim', models.CharField(max_length=200, verbose_name='lesson aim')),
                ('lalname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.add_lesson', verbose_name='lesson name')),
                ('lapnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.add_paragraph', verbose_name='paragph number')),
            ],
        ),
    ]
