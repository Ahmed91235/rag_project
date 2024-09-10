from fastapi import APIRouter, File, UploadFile, HTTPException, Depends,status
import os
import uuid
from fastapi.responses import JSONResponse
import aiofiles

from core.config import Settings, get_settings
from controller import DataController, ProjectController
data_router = APIRouter(prefix='/api/data')

# List of allowed MIME types

@data_router.post('/store/{project_id}')
async def store_file(project_id: str, file: UploadFile = File(...), app_settings: Settings = Depends(get_settings)):
    data_controller = DataController()
    
    is_valid, result = data_controller.validate_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content = {
                "signal": result
            }
        )
    
    try:
        
        file_path, file_id = data_controller.generte_uniqe_filepath(project_id=project_id, orig_file_name=file.filename)
        
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
        
        return {"filename": file_id , "message": "File stored successfully!"}
    
    except Exception as e:
        # Log the error (this can be extended with logging as described before)
        return {"message": "File upload failed. Please try again later."}
