from fastapi import UploadFile
import os
import re

from .BaseController import BaseController
from core.enums import EnumResponse
class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576
    
    
    def validate_file(self, file: UploadFile):
        
        # Check if the file's content type is allowed
        if file.content_type not in self.app_settings.ALLOWED_FILE_TYPES:
            return {"message": f"File type '{file.content_type}' is not allowed. Allowed types are: PDF, JPG, PNG, TXT"}
        
        # Check if the file's content size isn't exceeded the maximam size        
        if file.size > self.app_settings.ALLOWED_FILE_SIZE * self.size_scale:
            return {"message": f"File size '{file.size}' is exceeded the size. Allowed size is 10 MB"}
        
        return True, EnumResponse.FILE_VALIDATED_SUCCESS.value
        
        
    
    
            
    def generte_uniqe_filepath(self, project_id: str, orig_file_name: str):
        project_dir = os.path.join(
            self.files_dir,
            project_id
        )

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
            
        random_key = self.generate_random_string()
        clean_file_name = self.get_clean_file_name(orig_file_name=orig_file_name)
        new_file_name = random_key+"_"+clean_file_name
        file_path = os.path.join(
            project_dir,
            new_file_name
        )
        
        while os.path.exists(file_path):
            random_key = self.generate_random_string()
            file_path = os.path.join(
                project_dir,
                random_key+"_"+clean_file_name
            )
        
        return file_path, new_file_name
        
    def get_clean_file_name(self, orig_file_name: str):

        # remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())

        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name