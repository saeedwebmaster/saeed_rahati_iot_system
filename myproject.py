class Device:
    def __init__(self, topic):
        self.topic = topic
        self.topic_list = topic.split('/')
        self.location = self.topic_list[0]
        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.name = self.topic_list[3]
        self.status = 'off'  # وضعیت اولیه دستگاه خاموش است

    def turn_on(self):
        self.status = 'on'
        print(f'Device "{self.name}" is now ON.')

    def turn_off(self):
        self.status = 'off'
        print(f'Device "{self.name}" is now OFF.')

    def get_status(self):
        return self.status


class admin_panel:
    def __init__(self):
        self.groups = {}

    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'Group "{group_name}" created successfully.')
        else:
            print(f'Group "{group_name}" already exists.')

    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f'Device "{device.name}" added to group "{group_name}".')
        else:
            print(f'Group "{group_name}" does not exist.')

    def create_device(self, group_name, device_type, name):
        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f'Device "{name}" of type "{device_type}" created in group "{group_name}".')
        else:
            print(f'Group "{group_name}" does not exist.')

    def create_multiple_devices(self, group_name, device_type, number_of_devices):
        if group_name in self.groups:
            for i in range(1, number_of_devices + 1):
                device_name = f'{device_type}{i}'
                topic = f'home/{group_name}/{device_type}/{device_name}'
                new_device = Device(topic)
                self.add_device_to_group(group_name, new_device)
            print(f'{number_of_devices} devices of type "{device_type}" created in group "{group_name}".')
        else:
            print(f'Group "{group_name}" does not exist.')

    def get_devices_in_groups(self, group_name):
        if group_name in self.groups:
            return self.groups[group_name]
        else:
            print(f'Group "{group_name}" does not exist.')
            return []

    def turn_on_all_in_groups(self, group_name):
        devices = self.get_devices_in_groups(group_name)
        for device in devices:
            device.turn_on()
        print(f'All devices in group "{group_name}" turned on.')

    def turn_off_all_in_groups(self, group_name):
        devices = self.get_devices_in_groups(group_name)
        for device in devices:
            device.turn_off()
        print(f'All devices in group "{group_name}" turned off.')

    def turn_on_all_devices(self):
        for group_name, devices in self.groups.items():
            for device in devices:
                device.turn_on()
        print('All devices in all groups turned on.')

    def turn_off_all_devices(self):
        for group_name, devices in self.groups.items():
            for device in devices:
                device.turn_off()
        print('All devices in all groups turned off.')

    def get_status_in_group(self, group_name):
        if group_name in self.groups:
            devices = self.get_devices_in_groups(group_name)
            for device in devices:
                status = device.get_status()
                print(f'Device "{device.name}" in group "{group_name}" is {status}.')
        else:
            print(f'Group "{group_name}" does not exist.')

    def get_status_in_device_type(self, device_type):
        for group_name, devices in self.groups.items():
            for device in devices:
                if device.device_type == device_type:
                    status = device.get_status()
                    print(f'Device "{device.name}" in group "{group_name}" is {status}.')

    # توابع جدید
    def get_all_devices(self):
        all_devices = []
        for group_name, devices in self.groups.items():
            all_devices.extend(devices)
        return all_devices

    def remove_device_from_group(self, group_name, device_name):
        if group_name in self.groups:
            for device in self.groups[group_name]:
                if device.name == device_name:
                    self.groups[group_name].remove(device)
                    print(f'Device "{device_name}" removed from group "{group_name}".')
                    return
            print(f'Device "{device_name}" not found in group "{group_name}".')
        else:
            print(f'Group "{group_name}" does not exist.')


# تست کد
if __name__ == "__main__":
    # ایجاد یک پنل ادمین
    panel = admin_panel()

    # ایجاد یک گروه
    panel.create_group("living_room")

    # ایجاد چند دیوایس در گروه
    panel.create_multiple_devices("living_room", "lamp", 3)

    # روشن کردن تمام دیوایس‌ها در گروه
    panel.turn_on_all_in_groups("living_room")

    # دریافت وضعیت دیوایس‌ها در گروه
    panel.get_status_in_group("living_room")

    # خاموش کردن تمام دیوایس‌ها در گروه
    panel.turn_off_all_in_groups("living_room")

    # دریافت وضعیت دیوایس‌ها در گروه
    panel.get_status_in_group("living_room")