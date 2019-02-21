# flask-text-reader
Make text files like logs available for simple remote access via web browser.
## Instructions
1) Change the line `FILE_PATH=your_file_path_here` in the `.env` file including the path to the file you want to read (the file path is without quotes).
2) Run `pip install -r requirements.txt`
3) Run `bash run_gunicorn` or `bash run_flask_server` for debugging.
4) Your file content will be available on `http://your_ip:8050`.
## Instructions to install as a service
1) Create a unit file ending in .service within the /etc/systemd/system directory to begin:
`sudo vim /etc/systemd/system/flask-text-reader.service`
2) Fill the file with the data describing the service:
```
[Unit]
Description=Gunicorn instance to serve flask-text-reader
After=network.target

[Service]
User=user_name
WorkingDirectory=/home/user_name/flask-text-reader
Environment="PATH=/home/user_name/flask-text-reader/venv/bin"
EnvironmentFile=/home/user_name/flask-text-reader/.env
ExecStart=/home/user_name/flask-text-reader/venv/bin/gunicorn --bind 0.0.0.0:8050 app:app

[Install]
WantedBy=multi-user.target
```

**Tested on Python3**
