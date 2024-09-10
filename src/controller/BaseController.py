import random
import string
from core.config import Settings, get_settings
import os

class BaseController:
    
    def __init__(self) -> None:
        self.app_settings: Settings = get_settings()
        self.base_dir = os.path.dirname( os.path.dirname(__file__) )
        self.files_dir = os.path.join(
            self.base_dir,
            "assets/files"
        )
    
        
    def generate_random_string(self, length: int=12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))    