import argparse
import tidevice
from pprint import *

def cmd_battery(udid: str):
    d = tidevice.Device(udid=udid)
    power_info = d.get_io_power()
    if power_info['Status'] != 'Success':
        pprint(power_info)
        return

    info = power_info['Diagnostics']['IORegistry']
    indexs = (
        ('CurrentCapacity', '当前电量', '%'),
        ('Temperature', '电池温度', '°C'),
    )

    for keypath, cn_name, unit in indexs:
        value = info
        if isinstance(keypath, str):
            value = info[keypath]
            if keypath == 'Temperature':
                value = int(value) / 100
        else:
            value = info
            for key in keypath:
                value = value[key]
        if callable(unit):
            value = unit(value)
            unit = ''
        print("{:10s}{}{}".format(cn_name, value, unit))

def main():
    parser = argparse.ArgumentParser(description='get iOS battery info by tidevice')
    parser.add_argument('-u', '--udid', required=True, help='specify unique device identifier')
    args = parser.parse_args()
    if args.udid:
        cmd_battery(args.udid)
    else:
        print('请输入对应设备序列号的udid')


if __name__ == '__main__':
    main()
