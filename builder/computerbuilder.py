class Computer:
    def __init__(self,serial):
        self.serialnumber = serial
        self.model = None
        self.hdd = None
        self.gc = None

    def __str__(self):
        info = (f'Serial Number: {self.serialnumber}',
                f'Model : {self.model}',
                f'Memory : {self.hdd}',
                f'Graphic card : {self.gc}')
        return "\n".join(info)


class Tablet:

    def __init__(self, serial):
        self.serialnumber = serial
        self.model = None
        self.screensize = None
        self.hdd = None

    def __str__(self):
        info = (f'Serial Number: {self.serialnumber}',
                f'Model : {self.model}',
                f'Memory : {self.hdd}',
                f'screensize : {self.screensize}')
        return "\n".join(info)


class ComputerBuilder:
    serial = "AG"
    num = 23385193

    def __init__(self):
        serailnum = ComputerBuilder.serial + str(ComputerBuilder.num)
        self.computer = Computer(serailnum)
        ComputerBuilder.num+=1

    def configure_model(self, name):
        self.computer.model = name

    def configure_memory(self, memory):
        self.computer.hdd = memory

    def configure_gc(self,gc):
        self.computer.gc = gc


class TabletBuilder:
    serial = "AG"
    num = 23385193

    def __init__(self):
        serailnum = TabletBuilder.serial + str(TabletBuilder.num)
        self.tablet = Tablet(serailnum)
        TabletBuilder.num += 1

    def configure_model(self, name):
        self.tablet.model = name

    def configure_memory(self, memory):
        self.tablet.hdd = memory

    def configure_screensize(self, sz):
        self.tablet.screensize =sz


class HardwareEngineer:

    def __init__(self):
        self.builder = None

    def construct_computer(self, model, memory, gc):
        self.builder = ComputerBuilder()
        steps = (self.builder.configure_model(model),
                 self.builder.configure_memory(memory),
                 self.builder.configure_gc(gc))
        [step for step in steps]

    def construct_tablet(self, model, memory, sz):
        self.builder = TabletBuilder()
        steps = (self.builder.configure_model(model),
                 self.builder.configure_memory(memory),
                 self.builder.configure_screensize(sz))
        [step for step in steps]

    @property
    def computer(self):
        return self.builder.computer

    @property
    def tablet(self):
        return self.builder.tablet


def main():
    he = HardwareEngineer()
    he.construct_computer('Apple',4, 500)
    he.construct_computer('Mac', 5, 600)
    computer = he.computer
    print(computer)
    he.construct_tablet('mactablet',2,2000)
    tb = he.tablet
    print(tb)

if __name__== "__main__":
    main()
