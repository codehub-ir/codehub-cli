# codehub-cli
Simple [CodeHub](https://github.com/lnxpy/codehub) command-line client program uses API services. Start editing the `main.py` file then try to make your queries and run it up. There are two classes `GetSnippet` and `PushSnippet`. Just need to create an object.

##### Get a Snippet ⇒ `main.py`
```python
from components import GetSnippet

snippet = GetSnippet('usBVeMleZP')  # GetSnippet Obj
data = snippet.get()                # Data receiving
print(data)
```

##### Push a Snippet ⇒ `main.py`
```python
from components import PushSnippet

snippet = PushSnippet('TITL', 'DETAILS', 'SCRIPT', 'python') # PushSnippet Obj

try:
    result = snippet.push()                                  # Pushing process
    print('Snippet pushed!\n' + result['link'])
except Exception as e:
    print('Pushing failed for..\n', e)
```

#### Optionals
There are some fields you are able to leave them empty. `detail`and `error` fields are the optional parameters you may not want to fill them up, so you use the exact keywords to give other parameters the values you want.
```python
from components import GetSnippet, PushSnippet, Language

configs = {
    'title': 'TITLE',
    # 'details': 'DETAILS',  OPTIONAL PARAMETER
    'script': 'SCRIPT',
    # 'error': 'ERROR',      OPTIONAL PARAMETER
    'language': 'go',
}

snippet = PushSnippet(**configs).push()
print(snippet)
```
##### Language
You can also use `Language` class to use the default languages of the program. You may use a language is not listed in the `Language` class so write it by yourself. Other languages will be added soon.
```python
from components import PushSnippet, Language

lang = Language()
snippet = PushSnippet(..., lang.python) # Or PushSnippet(..., 'Prolog')
snippet.push()
```
<p align="center">
    <img src="https://github.com/lnxpy/CodeHub-cli/blob/master/git_components/lang.png">
</p>

### Develop it
Make changes in the main file or carry up the classes in your program. Don't forget the [GPL-3.0](https://github.com/lnxpy/codehub-cli/blob/master/LICENSE). Develop it for free :)
