import os
import configparser
import errno

from appdirs import user_config_dir, user_data_dir
from rich.console import Console
from rich.prompt import Prompt


APP_NAME = "jotpad"
APP_AUTHOR = "jotpad"

class Config:
    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read(os.path.join(f"{user_config_dir(APP_NAME)}", "config.ini"))






    
    def _write(self):
        with open(os.path.join(f"{user_config_dir(APP_NAME)}", "config.ini"), "w") as f:
            self._config.write(f)
    
    def is_initialized() -> bool:
        return "jotpad" in self._config

    def init(self):
        try:
            os.makedirs(user_config_dir(APP_NAME))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise RuntimeError("Unable to create config directory")

        if os.name == 'nt':
            preffered = "notepad"
            home_default = None  # AppData not working in windows
        else:
            preffered = "vi"
            home_default = user_data_dir(APP_NAME, APP_AUTHOR)
        
        if home_default:
            try:
                os.makedirs(home_default)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise RuntimeError("Unable to create data directory")

            home = Prompt.ask("Enter path to notes directory", default=home_default)
        else:
            home = Prompt.ask("Enter path to notes directory")
        editor = Prompt.ask(f"Enter preffered text editor", default=preffered)
        extension = Prompt.ask("Enter default file extension", default="txt")
        
        self._config["jotpad"] = {
            "home": home,
            "editor": editor,
            "default_extension": extension,
        }
        with open(os.path.join(f"{user_config_dir(APP_NAME)}", "config.ini"), "w") as f:
            self._config.write(f)
    
    @property
    def home(self):
        if "home" in self._config["jotpad"]:
            return self._config["jotpad"]["home"]
        
        
    @home.setter
    def home(self, value):
        self._config["jotpad"]["home"] = value
        self._write()
    
    @property
    def editor(self):
        return self._config["jotpad"]["editor"]

    @editor.setter
    def editor(self, value):
        self._config["jotpad"]["editor"] = value
        self._write()

    @property
    def default_extension(self):
        return self._config["jotpad"]["default_extension"]
    
    @default_extension.setter
    def default_extension(self, value):
        self._config["jotpad"]["default_extension"] = value
        self._write()
