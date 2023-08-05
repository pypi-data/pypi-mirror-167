from configparser import ConfigParser
from pathlib import Path
from sys import prefix
from typing import List,Any,Optional

class Setting(ConfigParser):
    host:str=""
    token:str=""
    ssl:bool=False
    __prefix__:str="/api/v1"
    baseurl:str=""
    __filename__:str=str(Path.home())+"/.mon-cli.ini"
        
    def __init__(self):
        super().__init__()        
        if not Path.exists(Path(self.__filename__)):
            with open(self.__filename__,"w+") as f:
                self["monitax"]={"host":"","token":"","ssl":"False"}
                self.write(f)
        self.read(self.__filename__)
        if self.has_option("monitax","host"):
            self.host=self.get("monitax","host")
        if self.has_option("monitax","token"):
            self.token=self.get("monitax","token")
        if self.has_option("monitax","ssl"):
            self.ssl=self.getboolean("monitax","ssl")
        self.baseurl=f"https://{self.host}{self.__prefix__}" if self.ssl else f"http://{self.host}{self.__prefix__}"      

    def setup(self,host:Optional[str]=None,token:Optional[str]=None,ssl:bool=False):
        if host is not None and token is not None:        
            self.set("monitax","host",host)
            self.set("monitax","token",token)
            self.set("monitax","ssl",str(ssl))                        
        elif host is not None:
            self.set("monitax","host",host)
            self.set("monitax","ssl",str(ssl))            
        elif token is not None:
            self.set("monitax","token",token)
            self.set("monitax","ssl",str(ssl))
        with open(self.__filename__,"w+") as configfile:
            self.write(configfile)

# if __name__=="__main__":
#     setting=Setting()



