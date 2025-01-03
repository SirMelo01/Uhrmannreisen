from django.shortcuts import render, redirect
from uhrmannreisen.ycms.models import FAQ, Message, TextContent, fileentry, Galerie, GaleryImage, Blog
import datetime
from django.http import HttpResponseRedirect


def load_index(request):
    faq = FAQ.objects.all()
    blog = Blog.objects.filter(active=True)

    context = {
        'FAQ': faq,
        'Blog': blog,
    }

    # Hero Section
    if TextContent.objects.filter(name="main_hero").exists():
        context["heroText"] = TextContent.objects.get(name='main_hero')
        
    if fileentry.objects.filter(place='main_hero').exists():
        context["heroImage"] = fileentry.objects.get(place='main_hero')

    # Angebote
    if TextContent.objects.filter(name="main_angebot").exists():
        context["angebotText"] = TextContent.objects.get(name='main_angebot')

    # News Section
    if TextContent.objects.filter(name="main_news").exists():
        context["newsText"] = TextContent.objects.get(name='main_news')

    # Busverkehr Section
    if TextContent.objects.filter(name="main_bus").exists():
        context["busText"] = TextContent.objects.get(name='main_bus')
        
    if fileentry.objects.filter(place='main_bus').exists():
        context["busImage"] = fileentry.objects.get(place='main_bus')
        
    # Busverkehr Untersection
    if TextContent.objects.filter(name="main_bus_text1").exists():
        context["busText1"] = TextContent.objects.get(name='main_bus_text1')
        
    if TextContent.objects.filter(name="main_bus_text2").exists():
        context["busText2"] = TextContent.objects.get(name='main_bus_text2')
        
    if TextContent.objects.filter(name="main_bus_text3").exists():
        context["busText3"] = TextContent.objects.get(name='main_bus_text3')
        
    # Tankstelle Section
    if TextContent.objects.filter(name="main_tanke").exists():
        context["tankeText"] = TextContent.objects.get(name='main_tanke')
        
    if fileentry.objects.filter(place='main_tanke').exists():
        context["tankeImage"] = fileentry.objects.get(place='main_tanke')
        
    # Tankstelle Untersection
    if TextContent.objects.filter(name="main_tanke_text1").exists():
        context["tankeText1"] = TextContent.objects.get(name='main_tanke_text1')
        
    if TextContent.objects.filter(name="main_tanke_text2").exists():
        context["tankeText2"] = TextContent.objects.get(name='main_tanke_text2')
        
    if TextContent.objects.filter(name="main_tanke_text3").exists():
        context["tankeText3"] = TextContent.objects.get(name='main_tanke_text3')

    # Tankstelle Section
    if TextContent.objects.filter(name="main_taxi").exists():
        context["taxiText"] = TextContent.objects.get(name='main_taxi')

    # Tankstelle Untersection
    if TextContent.objects.filter(name="main_taxi_text1").exists():
        context["taxiText1"] = TextContent.objects.get(name='main_taxi_text1')
        
    if TextContent.objects.filter(name="main_taxi_text2").exists():
        context["taxiText2"] = TextContent.objects.get(name='main_taxi_text2')
        
    if TextContent.objects.filter(name="main_taxi_text3").exists():
        context["taxiText3"] = TextContent.objects.get(name='main_taxi_text3')
        
    # Pflege Section
    if TextContent.objects.filter(name="main_pflege").exists():
        context["pflegeText"] = TextContent.objects.get(name='main_pflege')
        
    if fileentry.objects.filter(place='main_pflege').exists():
        context["pflegeImage"] = fileentry.objects.get(place='main_pflege')
        
    # Pflege Untersection
    if TextContent.objects.filter(name="main_pflege_text1").exists():
        context["pflegeText1"] = TextContent.objects.get(name='main_pflege_text1')
        
    if TextContent.objects.filter(name="main_pflege_text2").exists():
        context["pflegeText2"] = TextContent.objects.get(name='main_pflege_text2')
        
    if TextContent.objects.filter(name="main_pflege_text3").exists():
        context["pflegeText3"] = TextContent.objects.get(name='main_pflege_text3')
        
    # News Section
    if TextContent.objects.filter(name="main_news").exists():
        context["newsText"] = TextContent.objects.get(name='main_news')

    # Career Section
    if TextContent.objects.filter(name="main_career").exists():
        context["careerText"] = TextContent.objects.get(name='main_career')
        
    # Career Untersection
    if TextContent.objects.filter(name="main_career_1").exists():
        context["careerText1"] = TextContent.objects.get(name='main_career_1')
        
    if fileentry.objects.filter(place='main_career_1').exists():
        context["careerImage1"] = fileentry.objects.get(place='main_career_1')
        
    if TextContent.objects.filter(name="main_career_2").exists():
        context["careerText2"] = TextContent.objects.get(name='main_career_2')
        
    if fileentry.objects.filter(place='main_career_2').exists():
        context["careerImage2"] = fileentry.objects.get(place='main_career_2')

    # Galery
    if Galerie.objects.filter(place='main_bus').exists():
        galerie = Galerie.objects.get(place='main_bus')
        context["busGalery"] = galerie.images.all()

    if Galerie.objects.filter(place='main_tanke').exists():
        galerie = Galerie.objects.get(place='main_tanke')
        context["tankeGalery"] = galerie.images.all()

    if Galerie.objects.filter(place='main_pflege').exists():
        galerie = Galerie.objects.get(place='main_pflege')
        context["pflegeGalery"] = galerie.images.all()

    if Galerie.objects.filter(place='main_taxi').exists():
        galerie = Galerie.objects.get(place='main_taxi')
        context["taxiGalery"] = galerie.images.all()

    """ Galery
    if Galerie.objects.filter(place='main_hero').exists():
        context["heroImages"] = Galerie.objects.get(place='main_hero').images.all() """

    return render(request, 'pages/index.html', context=context)

def kontaktform(request):
    success = False
    current_date_time = datetime.datetime.now()
    if request.method == 'POST':
        Message.objects.create(name = request.POST["name"], email=request.POST['email'], message=request.POST['message'], date=current_date_time, seen=False)

        return render(request, 'pages/kontakt.html', {'success': True})

    return render(request, 'pages/kontakt.html', {'success': success})
