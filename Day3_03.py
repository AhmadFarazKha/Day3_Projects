from abc import ABC, abstractmethod
from collections import defaultdict

class SmartDevice(ABC):
    """
    #SmartHome #SmartDevice #AbstractClass 
    Abstract base class for all smart home devices.
    """
    def __init__(self, name, device_id, room, floor):
        self.name = name
        self.device_id = device_id
        self.room = room
        self.floor = floor
        self.status = "Offline"

    @abstractmethod
    def get_status(self):
        """
        #GetStatus #DeviceStatus 
        Abstract method to get the current status of the device.
        """
        pass

    def turn_on(self):
        """
        #TurnOn #DeviceControl 
        Turns the device on.
        """
        self.status = "On"

    def turn_off(self):
        """
        #TurnOff #DeviceControl 
        Turns the device off.
        """
        self.status = "Off"

class Light(SmartDevice):
    """
    #Light #SmartDevice 
    Class representing a smart light.
    """
    def __init__(self, name, device_id, room, floor, brightness):
        super().__init__(name, device_id, room, floor)
        self.brightness = brightness

    def get_status(self):
        """
        #LightStatus #DeviceStatus 
        Returns the current status of the light.
        """
        return f"Light '{self.name}' is {self.status} with brightness {self.brightness}"

class Thermostat(SmartDevice):
    """
    #Thermostat #SmartDevice 
    Class representing a smart thermostat.
    """
    def __init__(self, name, device_id, room, floor, temperature):
        super().__init__(name, device_id, room, floor)
        self.temperature = temperature

    def get_status(self):
        """
        #ThermostatStatus #DeviceStatus 
        Returns the current status of the thermostat.
        """
        return f"Thermostat '{self.name}' is {self.status} at {self.temperature} degrees"

class Camera(SmartDevice):
    """
    #Camera #SmartDevice 
    Class representing a smart camera.
    """
    def __init__(self, name, device_id, room, floor, recording):
        super().__init__(name, device_id, room, floor)
        self.recording = recording

    def get_status(self):
        """
        #CameraStatus #DeviceStatus 
        Returns the current status of the camera.
        """
        return f"Camera '{self.name}' is {self.status}, recording: {self.recording}"

class SmartHomeManager:
    """
    #SmartHomeManager #DeviceManagement 
    Class for managing smart home devices.
    """
    def __init__(self):
        self.devices = defaultdict(list)  # Group devices by room and floor

    def add_device(self, device):
        """
        #AddDevice 
        Adds a device to the system.
        """
        self.devices[(device.room, device.floor)].append(device)

    def get_devices(self):
        """
        #GetDevices 
        Returns all devices in the system.
        """
        return self.devices

    def get_devices_by_type(self, device_type):
        """
        #GetDevicesByType 
        Returns devices of a specific type.
        """
        return [device for room_devices in self.devices.values() for device in room_devices if isinstance(device, device_type)]

    def get_devices_by_status(self, status):
        """
        #GetDevicesByStatus 
        Returns devices with a specific status.
        """
        return [device for room_devices in self.devices.values() for device in room_devices if device.status == status]

    def execute_operation(self, devices, operation):
        """
        #ExecuteOperation #DeviceControl 
        Executes an operation (turn on/off) on a list of devices.
        """
        for device in devices:
            if operation == "turn_on":
                device.turn_on()
            elif operation == "turn_off":
                device.turn_off()

# Example Usage
manager = SmartHomeManager()

light1 = Light("Living Room Light", "L1", "Living Room", "Ground Floor", 50)
light2 = Light("Kitchen Light", "L2", "Kitchen", "Ground Floor", 30)
thermostat1 = Thermostat("Living Room Thermostat", "T1", "Living Room", "Ground Floor", 20)
camera1 = Camera("Front Door Camera", "C1", "Entrance", "Ground Floor", True)

manager.add_device(light1)
manager.add_device(light2)
manager.add_device(thermostat1)
manager.add_device(camera1)

# Get all lights
lights = manager.get_devices_by_type(Light)

# Get all active devices
active_devices = manager.get_devices_by_status("On")

# Turn off all lights
manager.execute_operation(lights, "turn_off")

# Print status of all devices
for room_devices in manager.get_devices().values():
    for device in room_devices:
        print(device.get_status())

