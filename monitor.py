import time
import wmi
import clr


file = r'C:\DESENVOLVIMENTO\Monitor de recursos W\OpenHardwareMonitor\OpenHardwareMonitorLib.dll'
clr.AddReference(file)

w = wmi.WMI(namespace = r"root\OpenHardwareMonitor")

teste = w.classes
while True:
    temperature_infos = w.Sensor()
    if len(temperature_infos) > 0:
        break
    time.sleep(1)
for sensor in temperature_infos:
    if sensor.SensorType==u'Temperature':
        print(sensor.Name)
        print(sensor.Value)