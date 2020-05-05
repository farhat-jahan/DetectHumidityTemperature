import RPi.GPIO as GPIO
# import com.farhat.dht11 as dht11
# import dht11
from dht11 import dht11
import time
import datetime
import psycopg2

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=17)

connection = psycopg2.connect(user="pi",
                                  password="chano@123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pi")

try:
    while True:
        result = instance.read()
        if result.is_valid():
            cursor = connection.cursor()

            postgres_insert_query = """ INSERT INTO SENSORPINGS (read_on, tempreature, humidity) VALUES (%s,%s,%s)"""
            record_to_insert = (datetime.datetime.now(), result.temperature, result.humidity)
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            # print (count, "Record inserted successfully into mobile table")
            # print("Last valid input: " + str(datetime.datetime.now()))
            #
            # print("Temperature: %-3.1f C" % result.temperature)
            # print("Humidity: %-3.1f %%" % result.humidity)

        time.sleep(1)
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
    connection.close()
