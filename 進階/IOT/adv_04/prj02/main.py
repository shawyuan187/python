import network

wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
ap.active(False)
wlan.active(True)
wlan.active(True)
wifil = wlan.scan()
print("scan result:")
for i in range(len(wifil)):
    print(wifil[i])
wlssid = "SingularClass"
wlp = "Singular#1234"
wlan.connect(wlssid, wlp)
while not (wlan.isconnected()):
    pass
print("network config:", wlan.ifconfig())
