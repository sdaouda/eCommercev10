from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Immobilier, Region, Localite, ImmageDB,Client,Vendor, ClientAlert
from django.contrib.auth import login as django_login, logout as django_logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from immoapp.forms import AddimageForm, ClientForm, AlertForm
#from bootstrap_modal_forms.generic import BSModalLoginView
#from .forms import CustomAuthenticationForm
#from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic.edit import UpdateView
from django.contrib import messages



# Create your views here.
def list_biens(request):
    lst = []
    categories = Category.objects.all()
    region = Region.objects.all()
    immobiliers = Immobilier.objects.filter(available=True)
    for bien in immobiliers:
        lst.append(bien.localite)
    localite_dispo = list(dict.fromkeys(lst))
    context={'categories':categories,'immobiliers':immobiliers,'localite_dispo':localite_dispo,'region':region,}
    #return render(request, 'immoSpace/base.html', context)
    return render(request, 'immoapp/index.html', context)

def list_biens1(request):
    lst = []
    categories = Category.objects.all()
    region = Region.objects.all()
    immobiliers = Immobilier.objects.filter(available=True)
    context={'categories':categories,'immobiliers':immobiliers,'region':region,}
    #return render(request, 'immoSpace/base.html', context)
    return render(request, 'immoapp/inventaire.html', context)

def details(request):
    context = {}
    return render(request, 'immoapp/details.html', context)

def addimage(request):
    imId =None
    categories = Category.objects.all()
    if request.method == 'POST':
        imId = int(request.POST['element'])
        origImage = request.POST
        form = AddimageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            form = AddimageForm(initial={'element': imId})
            return render(request, 'immoapp/add_image.html', {'categories': categories,
                                                                'form':form,
                                                                'origImage':origImage,})
        else:
            form = AddimageForm()
    else:
        form = AddimageForm()
        return render(request, 'immoapp/add_image.html', {'categories': categories,'form':form,})

def immodetail(request, id, goods_slug):
    categories = Category.objects.all()
    product = get_object_or_404(Immobilier, id=id, slug=goods_slug, available=True)
    pro = product.category.slug
    productsimilar = Immobilier.objects.filter(category__slug=pro, available=True).exclude(slug=goods_slug)
    imgsDB = ImmageDB.objects.filter(element=product.id)
    return render(request,'immoapp/details.html',{'product': product, 'imgsDB':imgsDB,
                                                         'categories': categories,'productsimilar':productsimilar,})

def addimage1(request, id):
    categories = Category.objects.all()
    form = AddimageForm(initial={'element': id,})
    return render(request, 'immoapp/add_image.html', {'categories': categories,
                                                            'form':form,})

def clientRecord(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        # request.POST['fullname']
        client_data = ClientForm(request.POST)
        if client_data.is_valid():
            client_data.save()
    return render(request, 'immoapp/client_response.html', {})

def alertRecord(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        # request.POST['fullname']
        alert_data = AlertForm(request.POST)
        if alert_data.is_valid():
            alert_data.save()
            messages.success(request, 'Contact request submitted successfully.')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, alert_data.errors)
        return redirect('/')
    # return render(request, 'immoapp/client_response.html', {})

class ClientAlertUpdateView(UpdateView):
    model = ClientAlert
    fields = ['created', 'alertname', 'lieux', 'typebien', 'typetransaction', 'budget', 'typecontact', 'alertcontact', 'commentaire']
    template_name_suffix = '_update_form'


def SearchList(request):
    queryset_list = Immobilier.objects.filter(available=True)
    categories = Category.objects.all()
    products = Immobilier.objects.filter(available=True)
    L_immo = Immobilier.objects.filter(available=True, action_type='LOCATION')
    V_immo = Immobilier.objects.filter(available=True, action_type='VENTE')
    act_immo = request.GET.get('actType')
    category = request.GET.get('category')
    region = request.GET.get('region')
    localite = request.GET.get('localite')

    # Afficher tout les biens
    if (act_immo == "Toutes" and category == "Toutes" and region == "Toutes" and localite == "Partout"):
        return render(request, 'immoapp/searchres.html', {'categories': categories, 'queryset_list': queryset_list, })

    # Afficher une vente ou une location par category, par region et par localite.
    elif (act_immo != "Toutes" and category != "Toutes" and region != "Toutes" and localite != "Partout"):
        queryset_list = queryset_list.filter(Q(localite__region__region__icontains=region), Q(localite__localite__icontains=localite),
                                                  Q(category__name__icontains=category), Q(action_type__iexact=act_immo))
        return render(request, 'immoapp/searchres.html', {'categories': categories, 'queryset_list': queryset_list,})

    # afficher les biens par category et par localites
    elif (act_immo == "Toutes" and category != "Toutes" and region != "Toutes" and localite != "Partout"):
        queryset_list = queryset_list.filter(Q(category__name__icontains=category), Q(localite__region__region__icontains=region), Q(localite__localite__icontains=localite))
        return render(request, 'immoapp/searchres.html', {'categories': categories, 'queryset_list': queryset_list,})

    # afficher les biens d une localite donnee
    elif (act_immo == "Toutes" and category == "Toutes" and region != "Toutes" and localite != "Partout"):
        queryset_list = queryset_list.filter(Q(localite__region__region__icontains=region), Q(localite__localite__icontains=localite))
        return render(request, 'immoapp/searchres.html', {'categories': categories, 'queryset_list': queryset_list,})

    # afficher les ventes ou les locations
    elif (act_immo != "Toutes" and category == "Toutes" and region == "Toutes" and localite == "Partout"):
        queryset_list = queryset_list.filter(Q(action_type__iexact=act_immo))
        return render(request, 'immoapp/searchres.html', {'categories': categories, 'queryset_list': queryset_list,})

    #location ou vente d une region donnee
    elif (act_immo == "Toutes" and category == "Toutes" and localite == "Partout" and region != "Toutes"):
        queryset_list = queryset_list.filter(Q(localite__region__region__icontains=region))
        return render(request, 'immoapp/searchres.html', {'categories': categories, 'queryset_list': queryset_list,})

    # afficher les ventes ou location par category
    elif (act_immo != "Toutes" and category != "Toutes" and region == "Toutes" and localite == "Partout"):
        queryset_list = queryset_list.filter(Q(category__name__icontains=category),
                                         Q(action_type__iexact=act_immo))
        return render(request, 'immoapp/searchres.html', {'categories': categories, 'queryset_list': queryset_list, })

    else:
        return render(request, 'immoapp/searchres.html', {'categories': categories, 'queryset_list': queryset_list, })


def newAlert(request):
    categories = Category.objects.all()
    return render(request, 'immoapp/alert_form.html', {'categories':categories,})

def Alertlist(request):
    categories = Category.objects.all()
    alerts = ClientAlert.objects.all()
    return render(request, 'immoapp/client_response.html', {'categories':categories,'alerts':alerts,})