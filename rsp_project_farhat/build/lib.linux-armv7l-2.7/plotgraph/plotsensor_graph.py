import psycopg2

# matplotlib pyplot module
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
# ax1 = fig.add_subplot(1, 1, 1)

connection = psycopg2.connect(user="pi",
                              password="chano@123",
                              host="10.0.0.36",
                              port="5432",
                              database="pi")
cursor = connection.cursor()
query = """ select * from (select * from SENSORPINGS order by read_on desc limit 10) fd order by read_on asc """
# plt.grid()
# plt.xticks(rotation=45, ha='right')
# plt.subplots_adjust(bottom=0.30)
# plt.title("Time vs Temp")
# plt.xlabel("Time")
# plt.ylabel("Temp")
ax1 = fig.add_subplot(1, 1, 1)

def animate(i):
    cursor.execute(query)
    data = cursor.fetchall()
    # print data
    timestmp, temp, humidity = zip(*data)
    time = ()
    for timeobj in timestmp:
        time += (timeobj.strftime("%m/%d, %H:%M:%S"),)
    ax1.clear()
    plt.grid()
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title("Time vs Temp")
    plt.xlabel("Time")
    plt.ylabel("Temp")
    ax1.plot(time, temp)


try:
    # print 'I am inside'
    ani = animation.FuncAnimation(fig, animate, interval=3000)
    plt.show()
except KeyboardInterrupt:
    print("Cleanup")
    connection.close()
# # retrieve the whole result set

# Create figure for plotting
# print (time, temp, humidity)

# the the x limits to the 'hours' limit
# plt.xlim(0, 23)
# set the X ticks every 2 hours
# plt.xticks(range(0, 23, 2))
# draw a grid

# set title, X/Y labels
# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()
# connection.close()