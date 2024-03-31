import network


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
