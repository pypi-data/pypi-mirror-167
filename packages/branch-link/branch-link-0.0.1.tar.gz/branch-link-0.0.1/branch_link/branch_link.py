from render_file_fullstackmqtt.render_fullstackmqtt import render as RD
from typing import Mapping, Any
from responsive.http import default_fobidden404 as DF404


class link(object):
    def __init__(self, settingPages : Mapping[str, Any]) -> None:
        self.__setting__ = settingPages
        self.__rd__ = RD(self.__setting__['phtml'], self.__setting__['pcss'], self.__setting__['pjs'])
        self.__dhtml__ = self.__rd__.dhtml
        self.__dcss__ = self.__rd__.dcss
        self.__djs__ = self.__rd__.djs
    
    def getDataSentisive(self, pagename):
        try:
            return self.__rd__.render(self.__setting__[pagename]['html'], self.__setting__[pagename]['css'], self.__setting__[pagename]['js'])
        except:
            return DF404()