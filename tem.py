from machine import Pin,ADC
import time
from ble_uart import BLE_UART

adc_pin = Pin(32)
adc = ADC(adc_pin)
adc.width(ADC.WIDTH_12BIT)
adc.atten(ADC.ATTN_11DB)

ble = BLE_UART("A8206026")

while True:
    vol = (adc.read()/4095)*3.6
    tem = (vol-0.5)*100
    print("目前溫度:", tem)
    ble.send('A8206026:'+ str(tem))
    time.sleep(1)
