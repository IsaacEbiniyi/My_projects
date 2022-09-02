from django.shortcuts import render
import json
import urllib.request

# Create your views here.


def index(request):

    if request.method == 'POST':
        city = request.POST['city']
        api_source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        list_of_data = json.loads(api_source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
                          + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            "icons":  list_of_data['weather'][0]['icon'],
        }
        print(data)

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})


# def coordinates(request):
#     city = request.POST['city']
#     api_source = urllib.request.urlopen(
#         'https://api.openweathermap.org/data/2.5/weather?q='+country_code+'&appid={API key}').read()
#     "https://api.openweathermap.org/data/2.5/weather?q={city name},{country code}&appid={API key}"
#
#     return render(request, "index.html", )


def zip_code(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?zip='+zip+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        list_of_data = json.loads(api_source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
                          + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            "icons":  list_of_data['weather'][0]['icon'],
        }
        print(data)

    else:
        city = ''
        data = {}
    return render(request, 'zip_code.html', {'city': city, 'data': data})

def ment(request):
    return render(request, "mental_index.html")


def home(request):
    return render(request, "index.html")


def news(request):
    return render(request, "news.html")


def healthy_foods(request):
    return render(request, "healthy_foods.html")


def stuffs(request):
    return render(request, "30 and 50.html")


def features_of_spinach(request):
    return render(request, "features_spainach.html")


def features_of_garlic(request):
    return render(request, "features_garlic.html")


def features_of_lemon(request):
    return render(request, "features_lemons.html")


def features_of_beetroots(request):
    return render(request, "features_beetroot.html")


def features_chocolates(request):
    return render(request, "features_chocolate.html")


def features_lentils(request):
    return render(request, "features_lentils.html")


def features_raspberry(request):
    return render(request, "features_raspberry.html")


def features_walnut(request):
    return render(request, "features_walnut.html")


def features_salmon(request):
    return render(request, "features_salmon.html")


def features_avocado(request):
    return render(request, "features_avocado.html")


def main(request):
    return render(request, "index.html")
