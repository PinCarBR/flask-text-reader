# flask-text-reader
Make text files like logs available for simple remote access via web browser.
## Instructions
1) Change the line `FILE_PATH=your_file_path_here` including the path to the file you want to read (the file path is without quotes).
2) Run `pip install -r requirements.txt`
3) Run `bash run_gunicorn` or `bash run_flask_server` for debugging.
4) Your file content will be available on `http://your_ip:8050`.
