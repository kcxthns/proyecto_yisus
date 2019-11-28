# Generated by Django 2.2.6 on 2019-11-28 16:20

from django.db import migrations, models
import torpedopage.validators


class Migration(migrations.Migration):

    dependencies = [
        ('torpedopage', '0012_apunte_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='apunte',
            name='descripcion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='apunte',
            name='documento',
            field=models.FileField(upload_to='media/documents', validators=[torpedopage.validators.validate_file_extension]),
        ),
    ]