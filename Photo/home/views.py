from django.shortcuts import render, redirect

from .models import Category , Photo
from .form import PhotoForm
# Create your views here.

def gallery(request):

    category = request.GET.get('category')

    if category != None:
         photos = Photo.objects.filter(category__name=category)
      
    else:
          photos = Photo.objects.all()
       

        


    categories = Category.objects.all()
    

    context = {'categories': categories , 'photos': photos}

    return render(request, 'photo/gellary.html', context)



def viewphoto(request,pk):

    photos = Photo.objects.get(id=pk)


    return render(request, 'photo/photo.html', {'photos':photos})



def addPhoto(request):
     
    category = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        if data['category'] != 'none':
            category = Category.objects.get(id= data['category'])

        elif data['category_new'] !='':
            category ,created = Category.objects.get_or_create(name = data['category_new'])

        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            discription =  data['discription'],
            image = image
        )
        return redirect('gallery')

    
        

    context = {'cetegories': category }
    return render(request, 'photo/add.html',context )


def detete(request,pk):

    photos = Photo.objects.get(id=pk)
    if request.method == "POST":
        photos.delete()
        return redirect('gallery')



    return render(request,"photo/delete.html", {'photos' : photos})