# Generated by Django 2.2.16 on 2022-08-06 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodgram', '0009_auto_20220806_0225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-id']},
        ),
    ]