from rpi_gpio_lib import GPIO


class L298NMotorCircuit:
    # motor A
    L298N_in1: int
    L298N_in2: int
    L298N_ena_1: int
    L298N_ena_2: int
    # PWM motor A
    L298N_ena_PWM: GPIO.PWM
    # motor B
    L298N_in3: int
    L298N_in4: int
    L298N_enb_1: int
    L298N_enb_2: int
    # PWM motor B
    L298N_enb_PWM: GPIO.PWM
    # purpose not specified
    L298N_CON5_1: int
    L298N_CON5_2: int

    def __init__(self, in1, in2, in3, in4, pwm_a, pwm_b):
        GPIO.setmode(GPIO.BOARD)
        self.L298N_in1 = in1
        self.L298N_in2 = in2
        self.L298N_in3 = in3
        self.L298N_in4 = in4
        self.L298N_ena_1 = pwm_a
        self.L298N_enb_1 = pwm_b
        GPIO.setup(self.L298N_in1, GPIO.OUT)
        GPIO.setup(self.L298N_in2, GPIO.OUT)
        GPIO.setup(self.L298N_in3, GPIO.OUT)
        GPIO.setup(self.L298N_in4, GPIO.OUT)
        GPIO.setup(self.L298N_ena_1, GPIO.OUT)
        GPIO.setup(self.L298N_enb_1, GPIO.OUT)
        self.init_ena_pwm_motor_a()
        self.init_enb_pwm_motor_b()

    def run_forward_motor_a(self):
        """
        spin motor A with clockwise movement
        :return: void
        """
        GPIO.output(self.L298N_in1, GPIO.HIGH)
        GPIO.output(self.L298N_in2, GPIO.LOW)

    def run_back_motor_a(self):
        """
        spin motor A with counterclockwise movement
        :return: void
        """
        GPIO.output(self.L298N_in1, GPIO.LOW)
        GPIO.output(self.L298N_in2, GPIO.HIGH)

    def stop_motor_a(self):
        """
        stop movement for motor A
        :return:
        """
        GPIO.output(self.L298N_in1, GPIO.LOW)
        GPIO.output(self.L298N_in2, GPIO.LOW)

    def run_forward_motor_b(self):
        """
        spin motor B with clockwise movement
        :return: void
        """
        GPIO.output(self.L298N_in3, GPIO.HIGH)
        GPIO.output(self.L298N_in4, GPIO.LOW)

    def run_back_motor_b(self):
        """
        spin motor B with counterclockwise movement
        :return: void
        """
        GPIO.output(self.L298N_in3, GPIO.LOW)
        GPIO.output(self.L298N_in4, GPIO.HIGH)

    def stop_motor_b(self):
        """
        stop movement for motor B
        :return:
        """
        GPIO.output(self.L298N_in3, GPIO.LOW)
        GPIO.output(self.L298N_in4, GPIO.LOW)

    def set_power_pwm_motor_a(self, dutycycle):
        self.L298N_ena_PWM.ChangeDutyCycle(dutycycle)

    def set_power_pwm_motor_b(self, dutycycle):
        self.L298N_enb_PWM.ChangeDutyCycle(dutycycle)

    def init_ena_pwm_motor_a(self, frequency=100):
        """
        :param frequency: Hz unit; 100Hz ~ 10ms period
        :return: void
        """
        self.L298N_ena_PWM = GPIO.PWM(self.L298N_ena_1, frequency)

    def init_enb_pwm_motor_b(self, frequency=100):
        """
        :param frequency: unit in Hz; 100Hz ~ 10ms period
        :return: void
        """
        self.L298N_enb_PWM = GPIO.PWM(self.L298N_enb_1, frequency)

