network = "192.268.10.0"
subnetmask = "255.255.255.0"

class Netz() :
    def __init__(self, network, subnetmask) :
        self.network = network
        self.subnetmask = subnetmask

    def getHosts(self) :
        pass


Lan1 = Netz("172.16.0.0", "/26")