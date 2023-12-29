from django.shortcuts import render
from django.urls import reverse
import time

from parsing_app.tasks import test1, test2, test3, test4, test_gecko, test_chrome


def index_page(request, n=0):
    start_time = time.time()
    data = {}

    if n == 1:
        test1.delay()

    if n == 2:
        test2.delay()

    if n == 5:
        test_gecko()

    if n == 6:
        test1.delay()
        test1.delay()

    if n == 7:
        test2.delay()
        test2.delay()


    end_time = time.time()
    work_time = end_time - start_time
    return render(request, 'index_page.html', {'data': data, 'work_time': work_time})
