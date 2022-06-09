# Generated by Django 3.2.3 on 2022-05-23 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requerimientos', '0002_initial'),
        ('agendamientos', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamiento',
            name='requerimiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='requerimientos.requerimiento'),
        ),
    ]