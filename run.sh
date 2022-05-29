#! /bin/bash

docker run --mount type=bind,source=/var/run/dbus/system_bus_socket,target=/var/run/dbus/system_bus_socket local/demo-bluetooth-scanpy
