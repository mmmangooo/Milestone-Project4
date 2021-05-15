from django.shortcuts import render


# Credit for code handling sending the user to custom 404 and 500
# error templates:
# https://github.com/GBrachetta/guillermo/blob/master/guillermo/views.py

def handler404(request, exception):
    """
    Handling 404 errors returning response with custom template
    """
    response = render(request, 'errors/404.html')
    response.status_code = 404
    return response


def handler500(request):
    """
    Handling 500 errors returning response with custom template
    """
    response = render(request, 'errors/500.html')
    response.status_code = 500
    return response
