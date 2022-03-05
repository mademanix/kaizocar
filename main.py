import control.steering.motor_steering as wheel
from modules.l298n_motor_circuit import L298NMotorCircuit
from utils.const import RPiGPIOExtendedBoardPinout

if __name__ == '__main__':
    L298N_MOTOR_MODULE_CIRCUIT_NOT_CLOSED = 0

    l298n_motor_circuit = L298NMotorCircuit(
        RPiGPIOExtendedBoardPinout.PIN_15_GPIO_22, RPiGPIOExtendedBoardPinout.PIN_16_GPIO_23,
        RPiGPIOExtendedBoardPinout.PIN_18_GPIO_24, RPiGPIOExtendedBoardPinout.PIN_22_GPIO_25,
        RPiGPIOExtendedBoardPinout.PIN_33_GPIO_13_PWM1, RPiGPIOExtendedBoardPinout.PIN_35_GPIO_19_PCM_FS
    )

    wheel_control = wheel.MotorSteering(l298n_motor_circuit)
    wheel_control.run_forward()
    wheel_control.run_back()
    wheel_control.turn_forward_left()
    wheel_control.turn_forward_right()
    wheel_control.turn_back_left()
    wheel_control.turn_back_right()
