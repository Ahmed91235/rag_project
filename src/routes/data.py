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
        # # Generate a unique filename using uuid
        # unique_filename = f"{uuid.uuid4()}_{file.filename}"
        
        # # Define the directory where the file will be stored: assets/files/{project_id}/
        # upload_dir = os.path.join("src", "assets", "files", project_id)
        
        # # Create the directory if it doesn't exist
        # os.makedirs(upload_dir, exist_ok=True)
        
        
        # # Save the file to the defined location
        # with open(file_path, "wb") as buffer:
        #     buffer.write(await file.read())
        print("1111111111111111111")
        file_path, file_id = data_controller.generte_uniqe_filepath(project_id=project_id, orig_file_name=file.filename)
        
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
        print("1111111111111111111")
        
        return {"filename": file_id , "message": "File stored successfully!"}
    
    except Exception as e:
        # Log the error (this can be extended with logging as described before)
        return {"message": "File upload failed. Please try again later."}
