# BluetoothScanpy
Example for bluetooth scanning with python for BLE and Standard bluetooth devices in Linux

The steps required for running the project are below if you are running it from the ***docker*** file or in your machine 
***directly*** only follow the marked steps required for your case.
## Setup
### Install dbus and bluetooth packages - [docker, directly]
Before run the project you should have `dbus` and `bluetooth` installed in your host machine. In most distros they should
be installed by default so this should be not needed for you.

For debian base distros you can install these packages as
```
    sudo apt-get install dbus bluetooth
```

For arch base distros you can install these packages as
```
    sudo pacman -S dbus bluetooth
```

After being installed be sure to have both running

debian base
```
    sudo service dbus start
    sudo service bluetooth start
```

arch base
```
    sudo systemctl start dbus
    sudo systemctl start bluetooth
```

**For other distros you should verify your distro package manager  for the appropriate packages

### Verify that you are using python3 [directly]

Verify that you have python3 installed

For debian base distros
```
    sudo apt-get install python3 python3-pip python3-venv
```

For arch base distros it should have come by default installed

### Install PyGObject dependencty [directly]
The easy way to get this dependency is to use the one from your distro repos

For debian base distros
```
    sudo apt-get install python3-gi
```

For arch base distros
```
    sudo pacman -S python-gobject
```

For more distro instructions fot this step you could refer to [PyGObject](https//pygobject.readthedocs.io/en/latest/getting_started.html)

## How to run [directly]

Be sure that your bluetooth and dbus service are running 

***DBUS*** for most no headless distros are required by several components. So, for most cases it should be running by
default on start. You must be carefully with no stopping this service because it would break a lot programs until restart.


1. For service base distros you can start them with
    ```
    service dbus start
    service bluetooth start
    ```

    For systemctl base systems it should be something like
    ```
    systemctl start  dbus
    systemctl start bluetooth
    ```
    
2. Then install the pydbus with pip
    ```
   pip3 install pydbus
   ```

3. Now you can run the application
    ```
   python3 main.py
   ```
It should show in your terminal something like this (with real macs)
```
...
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -93, data: {"RSSI": -93, "ManufacturerData": {"00": [1,2,32...], "0000": [241, 11]}}
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -71, data: {"RSSI": -71}
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -71, data: {"RSSI": -71, "ManufacturerData": {"00": [22, 8, 45]}}
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -87, data: {"RSSI": -87, "ManufacturerData": {"123": [255, 255, 255]}}
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -68, data: {"RSSI": -68}
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -66, data: {"RSSI": -66}
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -76, data: {"RSSI": -76}
...
```

## How to run [docker]
Be sure that your bluetooth and dbus service are running in your host machine before starting the docker

***DBUS*** for most no headless distros are required by several components. So, for most cases it should be running by
default on start. You must be carefully with no stopping this service because it would break a lot programs until restart.

1. Build the docker image
```
docker build -t local/demo-bluetooth-scanpy .
```
2. Then you can run your package
```
docker run --mount type=bind,source=/var/run/dbus/system_bus_socket,target=/var/run/dbus/system_bus_socket local/demo-bluetooth-scanpy
```

Is necessary to mount the system_bus_socket directory as bind so the container can access the system bus from your machine
to be able to communicate with the bluetooth device. For some cases you may need to verify some other options to run the
container without needing to give it access to the system bus since this can be a security risk.

3. It should show in your terminal something like this (with real macs)
```
...
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -93, data: {"RSSI": -93, "ManufacturerData": {"00": [1,2,32...], "0000": [241, 11]}}
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -71, data: {"RSSI": -71}
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -71, data: {"RSSI": -71, "ManufacturerData": {"00": [22, 8, 45]}}
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -87, data: {"RSSI": -87, "ManufacturerData": {"123": [255, 255, 255]}}
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -68, data: {"RSSI": -68}
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -66, data: {"RSSI": -66}
Event [change], MAC: FF:FF:FF:FF:FF:FF, RSSI: -76, data: {"RSSI": -76}
...
```



