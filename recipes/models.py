from django.db import models
from django.contrib.auth.models import User
 
class Category(models.Model):  
    name = models.CharField(max_length=65)

    def __str__(self):  ### ESSA FUNÇÃO DEFINE O CAMPO QUE "RETORNA" Ex: "title" COMO NOME A SER MOSTRADO NO ADMIN DO NAVEGADOR
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

                            #Criamos uma classe no models que pode ser entendida como uma "tabela" da base de dados

class Recipe(models.Model): #aqui definimos o nome da (classe/tabela) e ela tem que herdar de model.Model
    title = models.CharField(max_length=65)   # um campo para receber Título da Receita
    description = models.CharField(max_length=165) #um campo que armazena a descrição
    slug = models.SlugField()    
    preparation_time = models.IntegerField()                           ### AQUI ESTÃO SENDO DEFINIDAS AS "colunas" DA TABELA ###
    preparation_time_unit = models.CharField(max_length=65)            ### e como seus campos devem receber os dados ### 
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)    #o auto_now_add= gera uma data no momento da criação porém não mexe mais nessa data
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to="recipes/covers/%Y/%m/%d/", blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None,) #essa variável se relaciona com a tabela "categoria"  // on_delete quer dizerquando deletar set esse campo como nullo
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  #quando deletar set esse campo como nullo  ////#Criamos uma classe no models que pode ser entendida como a "tabela" da base de dados////

    def __str__(self):      ### ESSA FUNÇÃO DEFINE O CAMPO QUE "RETORNA" Ex: "title" COMO NOME A SER MOSTRADO NO ADMIN DO NAVEGADOR
        return self.title
    
