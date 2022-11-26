from django.db import models
from django.urls import reverse
from immoapp.slug import unique_slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url_vente(self):
        return reverse('ventecatbien', args=[self.slug])

    def get_absolute_url_location(self):
        return reverse('locationcatbien', args=[self.slug])


class Region(models.Model):
    region = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True, null=True)

    def __str__(self):
        return self.region


class Localite(models.Model):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True)
    localite = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True, null=True)

    def __str__(self):
        return "%s-%s" % (self.region, self.localite)


class Commodite(models.Model):
    name = models.CharField(max_length=30, help_text="Precisez un detail sur le bien")
    slug = models.SlugField(max_length=30, db_index=True, unique=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Immobilier(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.CharField(max_length=15, db_index=True, blank=True, null=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, null=True)
    dimmension = models.CharField(max_length=10, blank=True, null=True)
    localite = models.ForeignKey(Localite, on_delete=models.CASCADE, blank=True, null=True, verbose_name='localité')
    numeroParcelle = models.CharField(max_length=20, default="n/a", blank=True, null=True)
    lotissement = models.CharField(max_length=50, default="n/a", blank=True, null=True)
    actsession = models.CharField(max_length=15, blank=True, null=True)
    imageoriginal = models.ImageField(upload_to='immoapp/images/', blank=True, verbose_name='Image')
    description = models.TextField(blank=True, verbose_name='Decrire l immobilier svp')
    price = models.PositiveIntegerField(verbose_name='Prix')
    available = models.BooleanField(default=False)
    nbChambre = models.PositiveIntegerField(verbose_name='Nombre de Chambre(s)')
    nbDouche = models.PositiveIntegerField(verbose_name='Nombre de Douches(s)')
    ACT_TYPE = (
        ('LOCATION', 'LOCATION'),
        ('VENTE', 'VENTE'),
    )

    action_type = models.CharField(max_length=10, choices=ACT_TYPE, blank=True,
                                   default='LOCATION', help_text='Vente/Location', verbose_name='action')
    details = models.ManyToManyField(Commodite, help_text='Select a genre for this book', related_name='commodite', blank=True)
    created = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    createdBy = models.CharField(max_length=50, blank=True, null=True)
    vendeur = models.ForeignKey("Vendor", on_delete=models.CASCADE, blank=True, null=True)
    payment = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goodsdetails', args=[self.id, self.slug])


#     def get_absolute_url_modify(self):
#         return reverse('imodify', args=[self.id])
#     def get_absolute_url_delete(self):
#         return reverse('immmodelete', args=[self.id])
#     def line_total(self):
#         return self.price * 2
#     def line_total_agence(self):
#         return self.price / 2

class ImmageDB(models.Model):
    element = models.ForeignKey(Immobilier, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to='immoapp/img_database/', blank=True, help_text='Sélectionner une image svp..')

    def __str__(self):
        return str(self.img)


class Service(models.Model):
    name = models.CharField(max_length=50, blank=True, db_index=True)
    image = models.ImageField(upload_to='immoapp/service/images/', blank=True)
    description = models.TextField(blank=True, verbose_name='Description du service')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("Vendor", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, db_index=True, unique=True, null=True)
    idVendor = models.CharField(max_length=5, blank=True, null=True)
    email = models.EmailField()
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    phone3 = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    localite = models.ForeignKey(Localite, on_delete=models.CASCADE, blank=True, null=True, verbose_name='localité')
    commentaire = models.TextField(blank=True, verbose_name='D')

    def __str__(self):
        return self.name + "-" + self.phone1

    # def get_absolute_url(self):
    #     return reverse('shop:vendor-detail', args=[self.id])


class Client(models.Model):
    fullname = models.CharField(max_length=20)
    cellphone_number = models.CharField(max_length=25)

    def __str__(self):
        return self.cellphone_number

class ClientAlert(models.Model):
    created = models.CharField(max_length=15, blank=True, null=True)
    alertname = models.CharField(max_length=30)
    lieux = models.CharField(max_length=15, blank=True, null=True)
    typebien = models.CharField(max_length=15, blank=True, null=True)
    typetransaction = models.CharField(max_length=15, blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    typecontact = models.CharField(max_length=15, blank=True, null=True)
    alertcontact = models.PositiveIntegerField(verbose_name='Phone', blank=True, null=True)
    commentaire = models.TextField(blank=True, verbose_name='Information supplémentaire:')

    def __str__(self):
        return self.alertname

    def get_absolute_url(self):
        return reverse('alert_update', args=[self.id])

