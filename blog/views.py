from django.shortcuts import render

# Create your views here.
def blog(request):
    print('blog')

    context = {
    'text':'olar blog',
    'title':'Titulo do blog do Diego',
    }

    return render(
        request,
        'blog/index.html',
        context,
        )

def exemplo(request):
    print('exemplo')

    context = {
    'text':'olar exemplo',
    'title':'titulo do exemplo do Diego',
    }
    return render(
        request,
        'blog/exemplo.html',
        context,
        )
