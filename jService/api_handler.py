import urllib.request
import urllib.parse
import re
import json

class jService:
    def __init__(self):
        self.base_url = "http://jservice.io/api"

    def build_search_url(self, call_type: str, **kwargs) -> str:
        parameters = [(key, value) for key, value in kwargs.items()]
        url = self.base_url + f"/{call_type}"
        return url + "?" + urllib.parse.urlencode(parameters) if parameters else url

    def get_results(self, url: str) -> dict:
        response = None

        try:
            response  = urllib.request.urlopen(url)
            json_text = response.read().decode(encoding="utf-8")
            return json.loads(json_text)

        finally:
            if response != None:
                response.close()


if __name__ == '__main__':
    jservice = jService()
    url = jservice.build_search_url("random", count=4)
    print(url)
    results = jservice.get_results(url)
    for result in results:
        print(result['question'], result['answer'], sep=":   ")