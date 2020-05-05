import RPi.GPIO as GPIO
import dht11
import time
import datetime
import psycopg2

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
# read data using pin 17
instance = dht11.DHT11(pin=17)

connection = psycopg2.connect(user="**",
                                  password="**********",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pi")
try:
    print ('-->:Recording data every 1 sec from pin:GPIO17')
    while True:
        result = instance.read()
        if result.is_valid():
            cursor = connection.cursor()
            far_temp = format((result.temperature * 9 / 5) + 32, '.1f')
            postgres_insert_query = """ INSERT INTO 
                                        SENSORPINGS (read_on, temperature, humidity) 
                                        VALUES (%s,%s,%s)"""
            record_to_insert = (datetime.datetime.now(), far_temp, result.humidity)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
        time.sleep(1)
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
    connection.close()


# hosted machine address:
# ssh pi@10.0.0.36 -p 22
# File location
# /home/pi/home/pi/rsp_project_farhat/sensordata python store_sensordata.py
