# Generated by Django 4.2.1 on 2023-10-13 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_remove_portal_molding_molding_portal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=512)),
                ('door', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.door')),
            ],
        ),
    ]
