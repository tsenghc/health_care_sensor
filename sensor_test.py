from fdk300 import FDK300
from fdk400 import FDK400
from m170 import M170
from mtk_a1 import MTKA1
from collections import defaultdict

class HealthCare:
    def __init__(self,):
        self.sensor_data = {
            'weight':0,
            'pressure_S':0,
            'pressure_D':0,
            'pulse':0,
            'oxygen':0,
            'temperature':0
            }
        self.status = True
            
    def listen_sensor(self,):
        if self.sensor_data['temperature'] == 0:
            fdk300 = FDK300()
            _temp = fdk300.get_sensor_data()
            self.sensor_data['temperature'] = _temp['temperature']
        elif self.sensor_data['weight'] == 0:
            scale = MTKA1()
            _temp = scale.get_sensor_data()
            self.sensor_data['weight'] = _temp['weight']

        elif self.sensor_data['oxygen'] == 0:
            m170 = M170()
            _temp = m170.get_sensor_data()
            self.sensor_data['oxygen'] = _temp['oxygen']
            self.sensor_data['pulse'] = _temp['pulse']
        elif self.sensor_data['pressure_S'] == 0:
            fdk400 = FDK400()
            _temp = fdk400.get_sensor_data()
            self.sensor_data['pressure_S'] = _temp['pressure_S']
            self.sensor_data['pressure_D'] = _temp['pressure_D']

        return self.sensor_data


if __name__=='__main__':
    health_care=HealthCare()
    
    while health_care.status:
        health_care.listen_sensor()
        sensor_data = (health_care.sensor_data)
        print(sensor_data)
        if 0 not in sensor_data.values():
            print(sensor_data)
            break
