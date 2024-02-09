# Generated by Django 5.0.1 on 2024-02-06 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_soldproduct_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Mahsulotlar'},
        ),
        migrations.AlterModelOptions(
            name='soldproduct',
            options={'verbose_name_plural': 'Sotilgan mahsulotlar'},
        ),
        migrations.AlterModelOptions(
            name='warehouse',
            options={'verbose_name_plural': 'Omborxona'},
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
            preserve_default=False,
        ),
    ]
