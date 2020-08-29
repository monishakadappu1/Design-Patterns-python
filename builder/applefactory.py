MINI14 = '1.4GHz Mac mini'


class AppleFactory:
    class MacMin14:
        def __init__(self):
            self.memory = 4
            self.hdd = 500
            self.gpu = "Intel HD Graphics 5000"

        def __str__(self):
            info = ( f'Model:{MINI14}',
                     f'memory : {self.memory}',
                     f'Hard Disk : {self.hdd}',
                     f'Graphics card : {self.gpu}')
            return '\n'.join(info)

    def build_computer(self,model):
        if model==MINI14:
            return self.MacMin14()
        else:
            print("DOnt know how to build the model {}".format(model))


if __name__=="__main__":
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print(mac_mini)