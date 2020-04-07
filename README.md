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

### Develop it
Make changes in the main file or carry up the classes in your program. Don't forget the [GPL](https://github.com/lnxpy/codehub-cli/blob/master/LICENSE). Develop it for free :)
