from collections import defaultdict
class CondorManager:
    def __init__(self):
        self.telem_data = defaultdict(str)

    def process_packet(self, data: bytes) -> bytes:
        ddata = data.decode('utf-8')

        lines = ddata.splitlines()

        # Create a defaultdict
        datadict = defaultdict(str)  # Assuming all values are floats

        # Populate the defaultdict
        for line in lines:
            key, value = line.split('=')
            datadict[key] = value

        self.telem_data['src'] = 'CONDOR' #add source telemetry so base aircraft module knows where it came from if neededj
        self.telem_data['N'] = "unknown_aircraft" #TelemFFB is wholey dependant on knowing the aircraft.. will be a problem having different effects for different aircraft if its not part of the telemetry stream
        for key, value in datadict.items():
            # jump through some hoops to rename some keys, but preserve the order so that the default effects can use them unaltered, if needed
            if key == 'time':
                key = 'T'
            elif key == 'airspeed':
                key = 'TAS'

            self.telem_data[key] = value

        self.telem_data['VlctVectors'] = [self.telem_data[key] for key in ['vx', 'vy', 'vz']] #create vector list from discrete vector data
        self.telem_data['ACCs'] = [self.telem_data[key] for key in ['ax', 'ay', 'az']] #create vector list from discrete vector data

        packet = bytes(";".join([f"{k}={self.fmt(v)}" for k, v in self.telem_data.items()]), "utf-8") #format the output so the upstream telemetry manager knows how to decode it
        return packet
    def fmt(self, val):
        if isinstance(val, list):
            return "~".join([str(x) for x in val])
        return val

if __name__ == '__main__':
    f = open("condor_data.txt", "r")
    data = f.read()
    data = data.encode('utf-8')
    cd = CondorManager()
    print(cd.process_packet(data))
