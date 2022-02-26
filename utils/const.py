try:
    import RPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO

class MotorDCSupplyPower:
    # [F]irst [H]igh [S]econd [L]ow
    FHSL = [GPIO.HIGH, GPIO.LOW]
    # [F]irst [L]ow [S]econd [H]igh
    FLSH = [GPIO.HIGH, GPIO.LOW]
    # [F]irst [L]ow [S]econd [L]ow
    FLSL = [GPIO.HIGH, GPIO.LOW]
    # [F]irst [H]igh [S]econd [H]igh !! probably never used !!
    FHSH = [GPIO.HIGH, GPIO.LOW]


GEAR_STEP = 25


class MotorDCPWMPowerAccuracy:
    """
    current V DC / 100
    so for example: 3,3V input for motor circuit - 100%
    we want 1,6V - so 3,3 / 1,6 ~= 2 -> 50%
    max V DC = 12V
    """
    NO_POWER = 0
    LITTLE_POWER = 25
    HALF_POWER = 50
    GREAT_POWER = 75
    MAX_POWER = 100


class RPiGPIOBaseBoardPinout:
    PIN_1_3V3_POWER = 1
    PIN_2_5V_POWER = 2
    PIN_3_GPIO_2_SDA = 3
    PIN_4_5V_POWER = 4
    PIN_5_GPIO_3_SCL = 5
    PIN_6_GROUND = 6
    PIN_7_GPIO_4_GPCLK0 = 7
    PIN_8_GPIO_14_TXD = 8
    PIN_9_GROUND = 9
    PIN_10_GPIO_15_RXD = 10
    PIN_11_GPIO_17 = 11
    PIN_12_GPIO_18_PCM_CLK = 12
    PIN_13_GPIO_27 = 13
    PIN_14_GROUND = 14
    PIN_15_GPIO_22 = 15
    PIN_16_GPIO_23 = 16
    PIN_17_3V3_POWER = 17
    PIN_18_GPIO_24 = 18
    PIN_19_GPIO_10_MOSI = 19
    PIN_20_GROUND = 20
    PIN_21_GPIO_9_MISO = 21
    PIN_22_GPIO_25 = 22
    PIN_23_GPIO_11_SCLK = 23
    PIN_24_GPIO_8_CE0 = 24
    PIN_25_GROUND = 25
    PIN_26_GPIO_7_CE1 = 26


class RPiGPIOExtendedBoardPinout(RPiGPIOBaseBoardPinout):
    PIN_27_GPIO_0_ID_SD = 27
    PIN_28_GPIO_1_ID_SC = 28
    PIN_29_GPIO_5 = 29
    PIN_30_GROUND = 30
    PIN_31_GPIO_6 = 31
    PIN_32_GPIO_12_PWM0 = 32
    PIN_33_GPIO_13_PWM1 = 33
    PIN_34_GROUND = 34
    PIN_35_GPIO_19_PCM_FS = 35
    PIN_36_GPIO_16 = 36
    PIN_37_GPIO_26 = 37
    PIN_38_GPIO_20_PCM_DIN = 38
    PIN_39_GROUND = 39
    PIN_40_GPIO_21_PCM_DOUT = 40
