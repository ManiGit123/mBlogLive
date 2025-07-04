# Generated by Django 5.2.1 on 2025-06-12 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_financialblog_fin_date_financialblog_fin_image_and_more'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelblog',
            name='travel_date',
            field=models.DateField(null=True, verbose_name='Post date'),
        ),
        migrations.AddField(
            model_name='travelblog',
            name='travel_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='travelblog',
            name='travel_location',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='tutorialsblog',
            name='tuto_date',
            field=models.DateField(null=True, verbose_name='Post date'),
        ),
        migrations.AddField(
            model_name='tutorialsblog',
            name='tuto_duration',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='tutorialsblog',
            name='tuto_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='tutorialsblog',
            name='tuto_learner_type',
            field=models.CharField(choices=[('option1', 'Beginner'), ('option2', 'Intermediate'), ('option3', 'Advanced'), ('option4', 'Expert')], default='option1', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='financialblog',
            name='fin_date',
            field=models.DateField(null=True, verbose_name='Post date'),
        ),
        migrations.AlterField(
            model_name='financialblog',
            name='fin_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='financialblog',
            name='fin_type',
            field=models.CharField(choices=[('option1', 'Personal Finance'), ('option2', 'Investments'), ('option3', 'Retirement'), ('option4', 'Debt')], default='option1', max_length=50, null=True),
        ),
    ]
