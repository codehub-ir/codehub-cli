# codehub-cli
CodeHub Command-Line Interface Program Written in Python.

# Getting Snippet
```python
from components import GetSnippet

snippet = GetSnippet('usBVeMleZP')  # GetSnippet Obj
data = snippet.get()                # Data receiving
print(data)
```

## Pushing Snippet
```python
from components import PushSnippet

snippet = PushSnippet('TITL', 'DETAILS', 'SCRIPT', 'python') # PushSnippet Obj

try:
    result = snippet.push()                                  # Pushing process
    print('Snippet pushed!\n' + result['link'])
except Exception as e:
    print('Pushing failed for..\n', e)
```
