import mcu
wi= mcu.wifi('SingularClass', 'Singular#1234')
wi.setup(ap_active=False,sta_active=True)
wi.scan()
if wi.connect():
    print(f'ip={wi.ip}')