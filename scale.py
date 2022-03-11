import subprocess

class Scale:
    def __init__(self):
        self.cmd='''
        { printf 'scan on\n\n'
          printf '\n\n'
          sleep 30
          printf 'quit'
         
        } | bluetoothctl
        
        '''
        self.status=0
        
    def get_sensor_data(self):
        proc=subprocess.Popen(self.cmd,shell=True,stdout=subprocess.PIPE)

        for i in range(50):
            res=proc.stdout.readline()
            data=res.decode('ascii').strip()
            data_index=data.find('Device 6D:97:40:33:34:D0 ManufacturerData Value:')
            if self.status == 1:                
                raw_data=data.split(' ')
                raw_weight=raw_data[-9:-8]
                convert=int(raw_weight[0],16)/10
                self.status = 0
                return convert

            if data_index != -1:
                self.status = 1


if __name__=='__main__':
    scale=Scale()
    while 1:
        data=scale.get_sensor_data()
        print(data)
