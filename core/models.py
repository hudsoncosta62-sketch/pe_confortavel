from django.db import models

class clientes(models.Model):
    ESTADOS_CHIOCES: list[str] = [
        "AC", "Acre",
        "AL", "Alagoas",
        "AP", "Amapá",
        "AM", "Amazonas",
        "BA", "Bahia",
        "CE", "Ceará",
        "DF", "Distrito Federal",
        "ES", "Espírito Santo",
        "GO", "Goiás",
        "MA", "Maranhão",
        "MT", "Mato Grosso",
        "MS", "Mato Grosso do Sul",
        "MG", "Minas Gerais",
        "PA", "Pará",
        "PB", "Paraíba",
        "PR", "Paraná",
        "PE", "Pernambuco",
        "PI", "Piauí",
        "RJ", "Rio de Janeiro",
        "RN", "Rio Grande do Norte",
        "RS", "Rio Grande do Sul",
        "RO", "Rondônia",
        "RR", "Roraima",
        "SC", "Santa Catarina",
        "SP", "São Paulo",
        "SE", "Sergipe",
        "TO", "Tocantins"
    ]

    GENERO_CHOICES: list[str] = "M", "Masculino", "F", "Feminino", "O", "Outro"       
    CONTATO_CHOICES: list[str] = "Celular", "Celular", "Telefone Fixo", "Telefone Fixo", "Email", "Email", "Carta", "Carta", "Pessoalmente", "Pessoalmente"

    cpf= models.CharField(max_length=11, primary_key=True)
    nome= models.CharField(max_length=100)
    endereco= models.CharField(max_length=200)
    telefone= models.CharField(max_length=15)
    estado_domicilio= models.CharField(max_length=2, choices=ESTADOS_CHIOCES)
    cidade= models.CharField(max_length=50)
    genero= models.CharField(max_length=1, choices=GENERO_CHOICES)
    contato_preferencial= models.CharField(max_length=20, choices=CONTATO_CHOICES)
    email= models.EmailField(max_length=254, choices=CONTATO_CHOICES)
    nome_usuario= models.CharField(max_length=50, unique=True) 
    senha= models.CharField(max_length=128) 

    def save(self, *args, **kwargs):
        # Aqui você pode adicionar lógica para validar ou processar os dados antes de salvar
        self.nome_usuario = self.email
        super().save(*args, **kwargs)

class produtos(models.Model):
    COR_CHOICES: list[str] = [
        "Vermelho", "Vermelho",
        "Azul", "Azul",
        "Verde", "Verde",
        "Amarelo", "Amarelo", 
        "Preto", "Preto", 
        "Branco", "Branco"
    ]

    codigo= models.IntegerField(unique=True)
    nome= models.CharField(max_length=70)
    preco_compra= models.FloatField()
    preco_venda= models.FloatField()
    cor= models.CharField(max_length=20, choices=COR_CHOICES)
    data_fabricacao= models.DateField()
    imagem= models.ImageField(upload_to='produtos/')