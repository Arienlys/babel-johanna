# Generated by Django 3.0.2 on 2020-01-09 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20200108_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='type_publication',
            field=models.CharField(choices=[('_', 'Livres'), ('A', 'Autres'), ('M', 'Musique'), ('F', 'Films')], default='_', max_length=1),
        ),
    ]
