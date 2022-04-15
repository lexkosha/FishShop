from django.db import models

# Create your models here.


class SeoModel(models.Model):
    seo_title = models.CharField('Title', blank=True, max_length=250, unique=True)
    seo_description = models.CharField('Description', blank=True, max_length=250)
    seo_keywords = models.CharField('Keywords', blank=True, max_length=250)

    def get_seo_title(self):
        if self.seo_title:
            return self.seo_title
        return ''

    def get_seo_description(self):
        if self.seo_description:
            return self.seo_description
        return ''

    def get_seo_keywords(self):
        if self.seo_keywords:
            return self.seo_keywords
        return ''

    class Meta:
        abstract = True


class ProductCategory(SeoModel):
    slug = models.SlugField('Ссылка', max_length=50)
    name = models.CharField('Название', max_length=100, unique=True)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория продукты'
        verbose_name_plural = 'Категории продукты'


class Product(SeoModel):
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    name = models.CharField('Название', max_length=256)
    slug = models.SlugField('Ссылка', max_length=250)
    image = models.ImageField(upload_to='img_product', blank=True)
    description = models.TextField('Описание', blank=True)
    short_description = models.CharField('Краткое описание', max_length=70, blank=True)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2, default=0)
    sky = models.CharField('Артикул', max_length=6)
    quantity = models.PositiveIntegerField('Количество', default=0)
    is_published = models.BooleanField('Опубликовано', default=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ManufacturerProduct(SeoModel):
    name = models.CharField('Название', max_length=77, blank=True)
    description = models.CharField('Описание', max_length=500, blank=True)
    img_logo = models.ImageField('Логотип', upload_to='manufacturer', blank=True)
    products = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'



class ProductFeature(models.Model):
    code_product = models.IntegerField('Код товара', max_length=6, blank=True)
    color = models.CharField('Цвет', max_length=50, blank=True)
    img_color = models.ImageField('Цвет фото', upload_to='img_color', blank=True)
    heft = models.FloatField('Вес', max_length=5, blank=True)
    length = models.PositiveIntegerField('Длинна', blank=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return 'Свойство приманки'

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'
