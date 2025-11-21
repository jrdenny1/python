class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method to initialize the TV object.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to turn the TV on or off.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to mute or unmute the TV.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method to increase the TV channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    
    def channel_down(self) -> None:
        """
        Method to decrease the TV channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase TV volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
    
    def volume_down(self) -> None:
        """
        Method to decrease TV volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show the TV status.
        :return: TV status string.
        """
        if self.__muted:
            display_volume = Television.MIN_VOLUME
        else:
            display_volume = self.__volume

        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}'