# saxon-flask-api

## How to use this repo

1. Make venv `python3 -m venv env`
2. activate your virtual environemnt `source env/bin/activate`
3. Install requirements `pip install -r requirements.txt`
4. Export flask env variable `export FLASK_APP=app.py`
5. Run flask API `flask run`
6. Check console for no errors.
7. Call the api 2 times using 
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

The first call should succeed and return 
```
Article - My Article Authors: - Mr. Foo - Mr. Bar
```

The second one should fail and in the Flask logging you should see

```
 * Serving Flask app "app.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [19/Mar/2021 11:58:43] "POST /transform HTTP/1.1" 308 -
127.0.0.1 - - [19/Mar/2021 11:58:43] "POST /transform/ HTTP/1.0" 200 -
127.0.0.1 - - [19/Mar/2021 11:58:45] "POST /transform HTTP/1.1" 308 -
JNI_CreateJavaVM() failed with result: -5
```
