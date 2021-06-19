# from alytics.models import GraphFunc
from celery import shared_task

from alytics.celery import celery_app

import matplotlib.pyplot as plt
import numpy as np

import time
import datetime

 
# @shared_task
@celery_app.task
def create_graphic(graphfunc_id):

    def datetime_to_unixtime(date_time):
        return time.mktime(date_time.timetuple())

    gr = GraphFunc.objects.get(pk=graphfunc_id)

    start_dt = datetime_to_unixtime(datetime.datetime.now() - datetime.timedelta(days=gr.interval))
    end_dt = datetime_to_unixtime(datetime.datetime.now())

    tt = np.arange(start_dt, end_dt, gr.dt*60*60)

    text_func = gr.title

    y = np.array([eval(text_func) for t in tt])

    fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
    ax.plot(tt, y)
    fig.savefig('to.png')   # save the figure to file

    #plt.show()

    plt.close(fig)    # close the figure window



