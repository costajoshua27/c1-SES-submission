import urllib.request
import urllib.parse
import re
import json

class jService:
    def __init__(self):
        self.base_url = "http://jservice.io/api"

    def build_search_url(self, call_type: str, **kwargs) -> None:
        parameters = [(key, value) for key, value in kwargs.items()]
        url = self.base_url + f"/{call_type}"
        self.url = url + "?" + urllib.parse.urlencode(parameters) if parameters else url

    def get_results(self) -> dict:
        response = None

        try:
            response  = urllib.request.urlopen(self.url)
            json_text = response.read().decode(encoding="utf-8")
            return json.loads(json_text)

        finally:
            if response != None:
                response.close()


if __name__ == '__main__':
    jservice = jService()
    jservice.build_search_url("random", count=4)
    results = jservice.get_results()
    for result in results:
        print(result['question'], result['answer'], sep=":   ")