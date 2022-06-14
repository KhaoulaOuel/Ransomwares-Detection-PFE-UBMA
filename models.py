from django.db import models


class ModelFile(models.Model):
    filename = models.FileField(upload_to='myfiles/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return  str(self.filename)


class Resultat(models.Model):
    ModelsName = (
        ('Decision Tree', 'Decision Tree'),
        ('AdaBoost', 'AdaBoost'),
        ('Multi-Layer Perceptron', 'Multi-Layer Perceptron'),
        ('Support Vector Machine', 'Support Vector Machine'),
        ('Random Forest', 'Random Forest'),
        ('Logistic Regression', 'Logistic Regression'),
    )
    filename = models.ForeignKey(ModelFile, null=True, on_delete= models.SET_NULL,blank=True)
    model_name = models.CharField(max_length=200,null=True, choices=ModelsName,blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    result = models.CharField(max_length=500, null=True,blank=True)
    vector = models.CharField(max_length=500, null=True,blank=True)

    def __str__(self):
        if self is not None:
            return str(self.model_name+'___'+self.result)
