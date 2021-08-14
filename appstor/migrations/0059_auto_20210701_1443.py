# Generated by Django 3.1.3 on 2021-07-01 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0058_auto_20210701_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='strnubzah',
            name='juz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appstor.juznubzah'),
        ),
        migrations.AlterField(
            model_name='santri',
            name='jk',
            field=models.CharField(blank=True, choices=[('perempuan', 'perempuan'), ('laki-laki', 'laki-laki')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Mahad Aly', 'Mahad Aly'), ('Idadiyah', 'Idadiyah'), ('Tamhidiyah', 'Tamhidiyah')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strnubzah',
            name='halaman',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appstor.halnubzah'),
        ),
    ]
