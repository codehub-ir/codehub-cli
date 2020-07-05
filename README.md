# codehub-cli
Simple [CodeHub](https://github.com/lnxpy/codehub) command-line client program uses API services. Start editing the `main.py` file, then try to make your queries and run them up.

##### Get a Snippet ⇒ `main.py`
```python
from components import GetSnippet

snippet = GetSnippet('<SID>')       # GetSnippet Obj
data = snippet.get()                # Data receiving
print(data)
```

##### Push a Snippet ⇒ `main.py`
```python
from components import GetSnippet, PushSnippet, Language

configs = {
    'title': 'TITLE',
    'script': 'SCRIPT',
    'language': 'go',
}

snippet = PushSnippet(**configs).push()
print(snippet)
```

#### Optionals
There are some fields you are able to leave them empty. `detail` and `error` fields are the optional parameters you may not want to fill them up, so you use the exact keywords to give other parameters the values you want.
```python
from components import GetSnippet, PushSnippet, Language

configs = {
    'title': 'TITLE',
#   'details': 'DETAILS',  OPTIONAL PARAMETER
    'script': 'SCRIPT',
#   'error': 'ERROR',      OPTIONAL PARAMETER
    'language': 'go',
}

snippet = PushSnippet(**configs).push()
print(snippet)
```
##### Language
You can also use `Language` class to use the default languages of the program. You might use a language which is not listed in the `Language` class, so write it by yourself. **Up to 500 languages are available now.**
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
