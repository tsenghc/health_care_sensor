import sys

import pexpect


class FDK400:
    def __init__(self, device):
        self.device = device
        self.timeout = 1

    def connect(self,):
        try:
            self.child = pexpect.spawn("gatttool -I")
            self.child.sendline("connect {0}".format(self.device))
            self.child.expect("Connection successful", timeout=self.timeout)
            return True
        except:
            #print("Connect Fail")
            return False

    def get_pressure(self,) -> dict:
        connect_status = self.connect()
        if not connect_status:
            return False
        self.child.sendline("char-read-hnd 0x0023")
        self.child.expect("Characteristic value/descriptor:",
                          timeout=self.timeout)
        self.child.expect("\r\n", timeout=self.timeout)
        data=self.child.before.decode('ascii').strip().split()
        if len(data)==12:
            pressure_S=int(data[7],16)
            pressure_D=int(data[9],16)
            pulse=int(data[10],16)
            result={'pressure_S':pressure_S,'pressure_D':pressure_D,'pulse':pulse}
            return result
        

if __name__ == '__main__':
    import time
    while 1:
        fdk400 = FDK400("07:B3:EC:03:99:BE")
        pressure = fdk400.get_pressure()
        print(pressure)
        time.sleep(2)
