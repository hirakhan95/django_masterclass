from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect

articles = {
    'sports': 'SPORTS BILD',
    'finance': 'FINANCE ALERT',
    'art': 'THIS IS AN ART PAGE',
    'politics': 'YOU ARE ON POLITICS PAGE'
}


# Create your views here.
def news_view(request, topic):
    try:
        return HttpResponse(articles[topic])
    except:
        raise Http404('The page you requested is not found!')


def page_num_view(request, pg_num):
    topics_list = list(articles.keys())  # ['sports', 'finance', 'politics']
    topic = topics_list[pg_num]

    # print(topic)
    # return HttpResponse(str('asdasd'))

    return HttpResponseRedirect(topic)


def add_func(request, num1, num2):
    ad_res = num1 + num2
    res = f'The answer of {num1} and {num2} is {ad_res}'
    return HttpResponse(str(res))
