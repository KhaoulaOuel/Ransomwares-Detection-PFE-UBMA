# Generated by Django 4.0.4 on 2022-06-11 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_result_resultat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultat',
            name='filename',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.modelfile'),
        ),
        migrations.AlterField(
            model_name='resultat',
            name='model_name',
            field=models.CharField(blank=True, choices=[('Decision Tree', 'Decision Tree'), ('AdaBoost', 'AdaBoost'), ('Multi-Layer Perceptron', 'Multi-Layer Perceptron'), ('Support Vector Machine', 'Support Vector Machine'), ('Random Forest', 'Random Forest'), ('Logistic Regression', 'Logistic Regression')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='resultat',
            name='result',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='resultat',
            name='vector',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]