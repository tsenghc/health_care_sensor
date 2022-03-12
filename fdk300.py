import sys

import pexpect


class FDK300:
    def __init__(self, device):
        self.device = device
        self.timeout = 3

    def bytecode_convert(self, hex_code) -> list:
        strip_binary = (hex_code).decode('ascii').strip()
        hex_list = strip_binary.split(' ')
        return hex_list

    def connect(self,):
        try:
            self.child = pexpect.spawn("gatttool -I")
            self.child.sendline("connect {0}".format(self.device))
            self.child.expect("Connection successful", timeout=self.timeout)
            return True
        except:
            #print("Connect Fail")
            return False

    def get_temperature(self,) -> float:
        temperature = 0
        connect_status = self.connect()
        if not connect_status:
            #sys.exit()
            pass
        
        if connect_status:
            self.child.sendline("char-read-hnd 0x0024")
            self.child.expect("Characteristic value/descriptor:",
                              timeout=self.timeout)
            self.child.expect("\r\n", timeout=self.timeout)
            code = self.bytecode_convert(self.child.before)
            if len(code) == 8:
                mix_highlow_byte = code[4]+code[5]
                temperature = int(mix_highlow_byte, 16)/100
                if temperature < 50:
                    return {'temperature':temperature}
        return {'temperature':0}
        #print('wait scan...')


if __name__ == '__main__':
    import time
    while 1:
        fdk300 = FDK300("C6:05:04:07:4D:54")
        temperature = fdk300.get_temperature()
        print(temperature)
        time.sleep(2)
