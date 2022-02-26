import logging
from utils.const import MotorDCPWMPowerAccuracy, GEAR_STEP
from modules.l298n_motor_circuit import L298NMotorCircuit


class MotorSteering:
    # TODO describe MotorSteering constructor method more precisely and fill-up docs
    """
    motor dc engine steering module
    init module with GPIO pinouts
    """
    l298n_motor_circuit: L298NMotorCircuit
    current_gear_motor_a: int
    current_gear_motor_b: int

    def __init__(self, l298n_motor_circuit):
        logging.basicConfig(level=logging.INFO)
        self.l298n_motor_circuit = l298n_motor_circuit
        self.current_gear_motor_a = MotorDCPWMPowerAccuracy.MAX_POWER
        self.current_gear_motor_b = MotorDCPWMPowerAccuracy.MAX_POWER
        self._print_setup_configuration()

    def run_forward(self):
        self.l298n_motor_circuit.run_forward_motor_a()
        self.l298n_motor_circuit.run_forward_motor_b()

    def run_back(self):
        self.l298n_motor_circuit.run_back_motor_a()
        self.l298n_motor_circuit.run_back_motor_b()

    def turn_forward_left(self):
        self.l298n_motor_circuit.run_forward_motor_a()
        self.l298n_motor_circuit.stop_motor_b()

    def turn_forward_right(self):
        self.l298n_motor_circuit.stop_motor_a()
        self.l298n_motor_circuit.run_forward_motor_b()

    def turn_back_left(self):
        self.l298n_motor_circuit.run_back_motor_a()
        self.l298n_motor_circuit.stop_motor_b()

    def turn_back_right(self):
        self.l298n_motor_circuit.stop_motor_a()
        self.l298n_motor_circuit.run_back_motor_b()

    def gear_up_motor_a(self):
        if self.current_gear_motor_a >= MotorDCPWMPowerAccuracy.MAX_POWER:
            return
        self.l298n_motor_circuit.set_power_pwm_motor_a(self.current_gear_motor_a + GEAR_STEP)

    def gear_up_motor_b(self):
        if self.current_gear_motor_b >= MotorDCPWMPowerAccuracy.MAX_POWER:
            return
        self.l298n_motor_circuit.set_power_pwm_motor_b(self.current_gear_motor_b + GEAR_STEP)

    def gear_down_motor_a(self):
        if self.current_gear_motor_a <= MotorDCPWMPowerAccuracy.NO_POWER:
            return
        self.l298n_motor_circuit.set_power_pwm_motor_a(self.current_gear_motor_a - GEAR_STEP)

    def gear_down_motor_b(self):
        if self.current_gear_motor_b <= MotorDCPWMPowerAccuracy.NO_POWER:
            return
        self.l298n_motor_circuit.set_power_pwm_motor_b(self.current_gear_motor_b - GEAR_STEP)

    def _print_setup_configuration(self):
        logging.info(' -- successfully initialized MotorSteering module')
        logging.info(' -- pinouts setting:')
        logging.info(' ---- [left motor]')
        logging.info(' ------ IN1: {}'.format(self.l298n_motor_circuit.L298N_in1))
        logging.info(' ------ IN2: {}'.format(self.l298n_motor_circuit.L298N_in2))
        logging.info(' ------ PWM_A: {}'.format(self.l298n_motor_circuit.L298N_ena_1))
        logging.info(' ---- [right motor]')
        logging.info(' ------ IN3: {}'.format(self.l298n_motor_circuit.L298N_in3))
        logging.info(' ------ IN4: {}'.format(self.l298n_motor_circuit.L298N_in4))
        logging.info(' ------ PWM_B: {}'.format(self.l298n_motor_circuit.L298N_enb_1))
