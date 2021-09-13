from django.http import JsonResponse
def error_400(request, exception):
    return JsonResponse({ 'DATA': '','MESSAGE':'Error 400.', 'CODE' : 400})
def error_403(request, exception):
    return JsonResponse({ 'DATA': '','MESSAGE':'Error 403.', 'CODE' : 403})
def error_404(request, exception):
    return JsonResponse({'DATA': '', 'MESSAGE':'Error 404.', 'CODE' : 404})
def error_500(request):
    return JsonResponse({ 'DATA': '','MESSAGE':'Error 500.', 'CODE' : 500})