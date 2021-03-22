# saxon-flask-api

## How to use this repo

1. Make venv `python3 -m venv env`
2. activate your virtual environemnt `source env/bin/activate`
3. Install requirements `pip install -r requirements.txt`
4. Export flask env variable `export FLASK_APP=app.py`
5. Run flask API `flask run` or `python app.py`
6. Check console for no errors.
7. Call the api 1 time using 
```
curl --request POST \
  --url http://127.0.0.1:5000/transform \
  --header 'Content-Type: application/xml' \
  --data '<?xml version="1.0"?>
<Article>
  <Title>My Article</Title>
  <Authors>
    <Author>Mr. Foo</Author>
    <Author>Mr. Bar</Author>
  </Authors>
  <Body>This is my article text.</Body>
</Article>'
```

Example XSLT and XML are from https://developer.mozilla.org/en-US/docs/Web/API/XSLTProcessor/Basic_Example

The first call should fail like this: 

```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [22/Mar/2021 21:29:45] "POST /transform HTTP/1.1" 308 -
Error: failed to allocate an object
[JR_lazyJITCodeGen @ 1]: Failed to initialize lazy JIT compiler thread

JET RUNTIME HAS DETECTED UNRECOVERABLE ERROR: system exception at 0x00007f8119ee9d49
Please, contact the vendor of the application.
Core dump will be piped to "/usr/share/apport/apport %p %s %c %d %P %E"
Extra information about error is saved in the "jet_err_214896.txt" file.

[1]    214896 abort (core dumped)  python app.py
```
