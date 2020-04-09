import requests

config = {
    'main_address': 'http://codehub.pythonanywhere.com/api/',
    'api_version': 'v1'
}

URL = config['main_address'] + config['api_version'] + '/snippet/'


class GetSnippet:

    def __init__(self, SID):
        self.SID = SID

    def get(self):
        r = requests.get(URL + self.SID)
        return r.json()


class PushSnippet:

    def __init__(self, title, details, script, language):
        self.title = title
        self.details = details
        self.script = script
        self.language = language

    def push(self):
        structure = {
            'title': self.title,
            'detail': self.details,
            'script': self.script,
            'language': self.language,
        }
        r = requests.post(URL, json=structure)
        return r.json()


class Language:
    python = 'python'
    java = 'java'
    javascript = 'js'
    swift = 'swift'
    csharp = 'csharp'
    c = 'c'
    php = 'php'
    go = 'go'
