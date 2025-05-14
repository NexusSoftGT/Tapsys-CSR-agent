import sounddevice as sd
print(sd.query_devices(sd.default.device['input']))