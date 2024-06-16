import network
from machine import Pin, ADC, PWM
from umqtt.simple import MQTTClient
import sys


class gpio:
    def __init__(self):
        self._D0 = 16
        self._D1 = 5
        self._D2 = 4
        self._D3 = 0
        self._D4 = 2
        self._D5 = 14
        self._D6 = 12
        self._D7 = 13
        self._D8 = 15
        self._SDD3 = 10
        self._SDD2 = 9

    @property
    def D0(self):
        return self._D0

    @property
    def D1(self):
        return self._D1

    @property
    def D2(self):
        return self._D2

    @property
    def D3(self):
        return self._D3

    @property
    def D4(self):
        return self._D4

    @property
    def D5(self):
        return self._D5

    @property
    def D6(self):
        return self._D6

    @property
    def D7(self):
        return self._D7

    @property
    def D8(self):
        return self._D8

    @property
    def SDD2(self):
        return self._SDD2

    @property
    def SDD3(self):
        return self._SDD3


class wifi:
    def __init__(self, ssid=None, password=None):
        self.ssid = ssid
        self.password = password
        self.sta = network.WLAN(network.STA_IF)
        self.ap = network.WLAN(network.AP_IF)
        self.ap_active = False
        self.sta_active = False
        self.ip = None

    def setup(self, ap_active=False, sta_active=False):
        self.ap_active = ap_active
        self.sta_active = sta_active
        self.ap.active(ap_active)
        self.sta.active(sta_active)

    def scan(self):
        if self.sta_active:
            wifi_list = self.sta.scan()
            for i in range(len(wifi_list)):
                print(wifi_list[i][0])
        else:
            print("no sta")

    def connect(self, ssid=None, password=None) -> bool:
        ssid = ssid if ssid is not None else self.ssid
        password = password if password is not None else self.password
        if not self.sta_active:
            print("sta no")
            return False
        if ssid is None or password is None:
            print("wifi name or password is None")
            return False
        if self.sta_active:
            self.sta.connect(ssid, password)
            while not self.sta.isconnected():
                pass
            self.ip = self.sta.ifconfig()[0]
            print("network config:", self.sta.ifconfig())
            return True


class LED:
    def __init__(self, r_pin, g_pin, b_pin, pwm: bool = False):

        if pwm == False:
            self.RED = Pin(r_pin, Pin.OUT)
            self.GREEN = Pin(g_pin, Pin.OUT)
            self.BLUE = Pin(b_pin, Pin.OUT)
        else:
            freq = 1000
            dutyc = 0
            self.RED = PWM(Pin(r_pin), freq=freq, duty=dutyc)
            self.GREEN = PWM(Pin(g_pin), freq=freq, duty=dutyc)
            self.BLUE = PWM(Pin(b_pin), freq=freq, duty=dutyc)


class MQTT:
    def __init__(self, mqid, mqs, mqn, mqp):
        self.mqs = "mqtt.singularinnovation-ai.com"
        self.mqid = "lol"
        self.mqn = "singular"
        self.mqp = "Singular#1234"
        self.mqc = MQTTClient(mqid, mqs, user=mqn, password=mqp, keepalive=30)

    def connect(self):
        try:
            self.mqc.connect()
        except:
            sys.exit
        finally:
            print("nice")

    def subscribe(self, topic, on_message):
        self.mqc.set_callback(on_message)
        self.mqc.subscribe(topic)

    def chm(self):
        self.mqc.check_msg()
        self.mqc.ping()

    def publish(self, topic: str, msg: str):
        topic = topic.encode("utf-8")
        msg = msg.encode("utf-8")
        self.mqc.publish(topic, msg)


class servo:
    def __init__(self, sg_pin):
        self.sg_pin = PWM(Pin(sg_pin), freq=50, duty=0)

    def angle(self, angle: int):
        if 0 <= angle <= 180:
            self.sg_pin.duty(int(1023 * (0.5 + angle / 90) / 20))
