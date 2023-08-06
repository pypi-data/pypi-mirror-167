from pathlib import Path
from conans import ConanFile
from sense2.model.layout import Folders

class Sense2File(ConanFile):
    def __init__(self, output, runner, display_name="", user=None, channel=None):
        super().__init__(output, runner, display_name, user, channel)
        # layout() method related variables:
        self.folders = Folders()
        
    @property
    def deb_folder(self):
        return self.folders.base_deb
    
    @property
    def deb_path(self) -> Path:
        assert self.deb_folder is not None, "`deb_folder` is `None`"
        return Path(self.deb_folder)
    
    def install_deb(self):
        pass
    
    def install_docker(self):
        pass

    def install_sense_system(self):
        pass
    
    def upload_deb(sef):
        pass
