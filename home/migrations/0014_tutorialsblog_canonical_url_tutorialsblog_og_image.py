# Generated by Django 5.2.1 on 2025-05-25 03:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_tutorialsblog_alter_financialblog_options_and_more'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialsblog',
            name='canonical_url',
            field=models.URLField(blank=True, help_text="Leave blank to use the page's URL.", max_length=255, verbose_name='Canonical URL'),
        ),
        migrations.AddField(
            model_name='tutorialsblog',
            name='og_image',
            field=models.ForeignKey(blank=True, help_text='Shown when linking to this page on social media. If blank, may show an image from the page, or the default from Settings > SEO.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Preview image'),
        ),
    ]
