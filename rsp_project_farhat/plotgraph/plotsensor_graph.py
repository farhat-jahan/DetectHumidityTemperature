import psycopg2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use('fivethirtyeight')

connection = psycopg2.connect(user="**",
                              password="*********",
                              host="10.0.0.36",
                              port="5432",
                              database="pi")
cursor = connection.cursor()
query = """ select * from (select * from SENSORPINGS order by read_on desc limit 20) fd order by read_on asc """
fig, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
fig.suptitle("Time vs Temperature and Humidity")
ax1.grid(True)
ax2.grid(True)

def animate(i):
    cursor.execute(query)
    data = cursor.fetchall()
    timestmp, temp, humidity = zip(*data)
    time = ()
    for timeobj in timestmp:
        time += (timeobj.strftime("%m/%d, %H:%M:%S"),)
    ax1.clear()
    ax2.clear()
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.xlabel("Time")
    ax1.set(ylabel='Temperature(F)')
    ax1.plot(time, temp, 'tab:orange')
    ax2.set(ylabel='humidity %')
    ax2.plot(time, humidity)
try:
    ani = animation.FuncAnimation(fig, animate, interval=2000)
    plt.show()
except KeyboardInterrupt:
    print("Cleanup")
    connection.close()












