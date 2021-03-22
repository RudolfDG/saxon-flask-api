import requests

url = "http://localhost:5000/transform/"


for i in range(20000):
    payload = f"""<?xml version="1.0"?>
<Article>
  <Title>My Article {i}</Title>
  <Authors>
    <Author>Mr. Foo</Author>
    <Author>Mr. Bar</Author>
  </Authors>
  <Body>This is my article text.</Body>
</Article>
    """
    headers = {
      'Content-Type': 'application/xml'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(f"{i}: Got {response.status_code} in {response.elapsed.total_seconds()} seconds.")
