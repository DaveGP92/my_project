from django.db import models

from utils.date_time_models import TimeFieldModel

genre_choices = [
    ('M', 'male'),
    ('F', 'female')
]

class Customer(TimeFieldModel):
    name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50)
    dni = models.CharField(max_length=10, unique=True, null=False, blank=False)
    birthdate =  models.DateField(null=True, blank=True)
    address = models.CharField(max_length=50)
    genre = models.CharField(max_length=1, choices=genre_choices)

    class Meta():
        db_table = 'customers'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    

class Sale(TimeFieldModel):
    customer = models.ForeignKey(Customer, null=False, blank=False, on_delete=models.CASCADE, db_column='cuetomer_id', related_name='sales')
    sell_date = models.DateTimeField(null=True)
    subtotal = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    iva = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    total = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    class Meta():
        db_table = 'sales'
        verbose_name = 'sale'
        verbose_name_plural = 'sales'
    
    def __str__(self):
        return int(self.total)
    

class Category(TimeFieldModel):
    name = models.CharField(max_length=50, null=False, blank=False)

    class Meta():
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    

class Product(TimeFieldModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id', related_name='products')
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(null=True)
    retail_price = models.DecimalField(null=False, max_digits=6, decimal_places=2)

    class Meta():
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.category
    

class SaleDetail(TimeFieldModel):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, db_column='sale_id', related_name='sale_detail')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id', related_name='product_detail')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta():
        db_table = 'sale_details'
        verbose_name = 'sale detail'
        verbose_name_plural = 'sale details'
    
    def __str__(self):
        return f"{self.product.name}, sold: {self.quantity}"


