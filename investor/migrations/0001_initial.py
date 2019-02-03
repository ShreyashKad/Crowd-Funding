# Generated by Django 2.1.1 on 2019-02-03 03:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_funding', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('amount', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('contact', models.FloatField()),
                ('gender', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('company', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('pic_path', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='funding',
            name='investor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='investor.Investor'),
        ),
        migrations.AddField(
            model_name='funding',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='student.Project'),
        ),
    ]
