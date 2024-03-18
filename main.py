import paho.mqtt.client as mqtt

def ao_conectar (client, userdata, flags, rc):
    print ("Nós conectamos com o seguinte código de resultado {}".format (str(rc)))

def ao_receber (client, userdata, msg):
     print ("{} --- {}". format (msg.topic, str(, msg.payload)))
