from celery import shared_task


@shared_task
def adding_task(x, y):  
    return x + y


import matplotlib.pyplot as plt
import numpy as np

import time
import datetime

interval = 30 # days
dt = 2 # hours

def datetime_to_unixtime(date_time):
    return time.mktime(date_time.timetuple())


start_dt = datetime_to_unixtime(datetime.datetime.now() - datetime.timedelta(days=interval))
end_dt = datetime_to_unixtime(datetime.datetime.now())

tt = np.arange(start_dt, end_dt, dt*60*60)

text_func = input('y(t)=')

y = np.array([eval(text_func) for t in tt])

fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.plot(tt, y)
fig.savefig('to.png')   # save the figure to file

#plt.show()

plt.close(fig)    # close the figure window
