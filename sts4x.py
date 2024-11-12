# bmp.py
# Copyright (c) 2024 by Jun-Wei Chang.
# All rights reserved.
# Released under creative commons attribution CC BY-NC-SA.

from machine import Pin, I2C
import ustruct
import time

class STS4X():
    # STS4X's I2C address
    __STS4X_ADDR = 0x44

    # Commands
    __MEASURE_T_HIGH_PRECISION = 0xFD
    __MEASURE_T_MEDIUM_PRECISION = 0xF6
    __MEASURE_T_LOWEST_PRECISION = 0xE0
    __READ_SERIAL = 0x89
    __SOFT_RESET = 0x94

    def __init__(self, i2c_addr = __STS4X_ADDR, i2c_id = 0, scl_pin = 17, sda_pin = 16):
        # Set i2c pins and initialize
        self.i2c = I2C(i2c_id, scl=Pin(scl_pin), sda=Pin(sda_pin))
        self.i2c_addr = i2c_addr
        return None

    def __write_command(self,cmd):
        self.i2c.writeto(self.i2c_addr,bytes([cmd]))
        # return ustruct.unpack(">h",data_bytes)[0]
        return

    def __read_data(self,len):
        data_bytes = self.i2c.read(len)
        return data_bytes
    
    def get_high_precision_temp_bytes(self):
        self.__write_command(self.__MEASURE_T_HIGH_PRECISION)
        time.sleep(0.01)
        data_bytes = self.__read_data(3)
        return data_bytes

    def get_medium_precision_temp_bytes(self):
        self.__write_command(self.__MEASURE_T_MEDIUM_PRECISION)
        time.sleep(0.01)
        data_bytes = self.__read_data(3)
        return data_bytes

    def get_lowest_precision_temp_bytes(self):
        self.__write_command(self.__MEASURE_T_LOWEST_PRECISION)
        time.sleep(0.01)
        data_bytes = self.__read_data(3)
        return data_bytes

    def get_serial_number_bytes(self): 
        self.__write_command(self.__READ_SERIAL)
        time.sleep(0.01)
        data_bytes = self.__read_data(6)
        return data_bytes

    def soft_reset(self):
        self.__write_command(self.__SOFT_RESET)