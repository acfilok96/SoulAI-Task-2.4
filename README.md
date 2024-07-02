## Database Details

-  **Database engin:** `Image_Record_SQLDB.db`
-  **Table:** `Image_Record_SQLDB_TABLE`

## Folder Set up

`Folder`

  `├── Image_Record_SQLDB.db`
  
  `├── main.py`
  
  `├── requirements.txt`

Download the `Folder` file & open it in `Visual Studio Code`. Open  `terminal` and run there

## How to run

-  **Run on terminal:**
  
\> `uvicorn main:app --reload`

-  run the FastAPI server using: `uvicorn main:app --reload` where filename is `main.py` 
-  Replace main with your script name if different. This command starts the server on http://127.0.0.1:8000.

## Accessing the API
-  Open a web browser or use tools like curl or Postman.
-  Navigate to `http://127.0.0.1:8000/image-summary/{filename}`, where `{filename}` is the image filename you want to retrieve the summary for.
-  Example: `http://127.0.0.1:8000/image-summary/4.jpg` & this will return summary about image.
