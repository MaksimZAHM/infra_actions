from django.http import HttpResponse


def index(request):
    return HttpResponse('Ура, у меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
