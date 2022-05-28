import os

from gi.repository import GLib
from datetime import datetime
import pydbus
import json
import re

HCI_INTERFACE = "hci0"
if "HCI_INTERFACE" in os.environ:
    HCI_INTERFACE = os.environ["HCI_INTERFACE"]


def extract_mac(device):
    match = re.search('dev_(?P<mac>.*)', device)
    if match is None:
        return None
    return match.group('mac').replace('_', ':')


def update_device(device, data):
    timestamp = datetime.utcnow().isoformat()
    mac = extract_mac(device)
    if mac is None:
        return
    message = f'MAC: {mac}, RSSI: {data["RSSI"]}, data: {json.dumps(data)}'
    print(message)


def on_change(sender, object, iface, signal, params):
    if 'org.bluez.Device1' != params[0]:
        return

    device = object
    data = params[1]
    print("Event: [change], ", end='')
    update_device(device, data)


def on_add(sender, object, iface, signal, params):
    if 'org.bluez.Device1' not in params:
        return

    device, data_dict = params
    data = data_dict[device]
    print("Event: [add], ", end='')
    update_device(device, data)


def main():
    bus = pydbus.SystemBus()
    bluez = bus.get("org.bluez", f"/org/bluez/{HCI_INTERFACE}")
    bus.subscribe(signal_fired=on_add, iface='org.freedesktop.DBus.ObjectManager', signal='InterfacesAdded')
    bus.subscribe(signal_fired=on_change, iface="org.freedesktop.DBus.Properties", signal="PropertiesChanged")
    loop = GLib.MainLoop()

    print("Setting filter...")
    bluez.SetDiscoveryFilter({
        'Transport': GLib.Variant('s', 'le'),
        'DuplicateData': GLib.Variant('b', True)
    })
    print("Starting discovery...")
    bluez.StartDiscovery()
    loop.run()


main()
