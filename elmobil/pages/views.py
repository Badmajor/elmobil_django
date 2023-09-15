from django.shortcuts import render


def about(request):
    template = 'pages/about.html'
    context = dict(
        SITE_NAME='elmobil.ru',
        TITLE_FROM_INDEX='Электромобили: преимущества, технологии и перспективы развития'
    )
    return render(request, template, context)
