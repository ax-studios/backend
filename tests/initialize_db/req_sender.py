import requests


def send_request(request_str):
    url = "http://127.0.0.1:5000/graphql"

   
    response = requests.post(url=url, json={"query": request_str})
    if response.status_code == 200:
        return response.content

    else:
        raise RequestError(str(response.status_code))


class RequestError(Exception):
    pass
