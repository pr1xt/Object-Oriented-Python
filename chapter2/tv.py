class tv():
    def __init__(self):
        self.isOn = False
        self.getInfo = False
        self.volume = 0
        self.channelindex = 0
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.VOLUME_MINIMUM = 0 # constant
        self.VOLUME_MAXIMUM = 10 # constant

    def turnPower(self):
        if self.isOn == True:
            self.isOn = False
        else:
            self.isOn = True

    def turnMute(self):
        if self.volume == self.VOLUME_MINIMUM:
            self.volume = self.VOLUME_MAXIMUM
        else:
            self.volume = self.VOLUME_MINIMUM

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
            # if the newChannel is not in our list of channels, don't do anything

