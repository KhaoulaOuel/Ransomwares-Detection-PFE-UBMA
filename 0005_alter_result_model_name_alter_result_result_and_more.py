# Generated by Django 4.0.4 on 2022-06-11 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_file_modelfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='model_name',
            field=models.CharField(choices=[('Decision Tree', 'Decision Tree'), ('AdaBoost', 'AdaBoost'), ('Multi-Layer Perceptron', 'Multi-Layer Perceptron'), ('Support Vector Machine', 'Support Vector Machine'), ('Random Forest', 'Random Forest'), ('Logistic Regression', 'Logistic Regression')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='result',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name='Models',
        ),
    ]
