from django.http import HttpResponse

def index(request):
    return HttpResponse(" sumar/a/b , restar/a/b, multiplicar/a/b")
def sumar(request, n1, n2):
    sumar = n1 + n2
    return HttpResponse("La suma de {} + {} =  {}".format(n1,n2,sumar))
def restar(request, n1, n2):
    restar = n1 - n2
    return HttpResponse("La resta de {} - {} =  {}".format(n1,n2,restar))
def multiplicar(request, n1, n2):
    multiplicar = n1 * n2
    return HttpResponse("La multiplicacion de {} * {} =  {}".format(n1,n2,multiplicar))
