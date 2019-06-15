# flask-starter
Basic Flask app for start project faster. Just clone the repo and start create your own flask app. No more no less

- in "main.py" you will find just 2 possible routing of FlaskApp

- accessible endpoint for this starter:
```
Hello World:
http://127.0.0.1:5000/
Will return: "Hello world!"

Hello with name:
http://127.0.0.1:5000/welcome/your_name_here
Will return: "Hello your_name_here!, welcome to this Flask App!!"
```

- For run the application, go to the main.py location and do the following commands:
```
export FLASK_APP=main.py
flask run
```

There are few incompatibility with python3. For resolve them, use the following commands:

```
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8
```
For more info about the incompatibility with python3 check [this](https://click.palletsprojects.com/en/7.x/python3/) link
