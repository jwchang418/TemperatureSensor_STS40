# MicroPython module for STS4x temperature sensor

The STS40 is a compact, high-accuracy temperature sensor. It communicates with the MCU via an I2C interface, supporting speeds of up to 400 kHz. The sensor is easy to use, requiring only a few commands to retrieve measurement data. In this demonstration, we utilize the MicroPython module on the Raspberry Pi Pico to display the data obtained from the STS40 temperature sensor.
<br>

## Pin Connection
| raspberry pi pico w | | STS40_PCB_Module|
| :---:| :---: |:---: |
| VBUS | -> | VCC |
| Gnd | -> | GND |
| GP16 | -> | SDA |
| GP17 | -> | SCL |
<br>

## Quick Start
Save the code as [__main.py__](./main.py) and [__sts4x.py__](./sts4x.py) files into the raspberry pi pico.
<br>

## Class STS4x
### Constructor

    class sts4x.STS4x( [i2c_addr = __APDS9151_ADDR],
                     [i2c_id = 0],
                     [scl_pin = 17],
                     [sda_pin = 16] )

Construct a new STS4x object with the given arguments:
* __i2c_addr__ The i2c address of the STS4x series (optional)
* __i2c_id__ The i2c ID of the pi pico (optional)
* __scl_pin__ The pin of the scl (optional)
* __sda_pin__ The pin of the sda (optional)

### Method

    class sts4x.get_high_precision_temp_bytes()
This method is applied to extract the high precision temperature data bytes, which consist of two bytes of the original sensing data and one byte for the CRC8 checksum.

    class sts4x.get_medium_precision_temp_bytes()
This method is applied to extract the medium precision temperature data bytes, which consist of two bytes of the original sensing data and one byte for the CRC8 checksum.
    
    class sts4x.get_lowest_precision_temp_bytes()
This method is applied to extract the low precision temperature data bytes, which consist of two bytes of the original sensing data and one byte for the CRC8 checksum.
    
    class sts4x.get_serial_number_bytes()
This method is applied to extract the serial number bytes from STS4x, where the data package consists of two bytes for the serial number, one byte for the CRC8 checksum, followed by two more bytes for the serial number and one byte for the checksum.
    
    class sts4x.soft_reset()
This method is used to reset the STS4x.
<br>

## Reference
* Raspberry Pi Pico
https://www.raspberrypi.com/products/raspberry-pi-pico/
* STS4x series data sheet
https://sensirion.com/media/documents/D2D0B4A9/667AC1F4/HT_DS_Datasheet_STS4x.pdf
* MicroPython i2c
https://docs.micropython.org/en/latest/library/machine.I2C.html
<br>

## license
Licensed under creative commons attribution __CC BY-NC-SA__