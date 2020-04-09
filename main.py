from components import GetSnippet, PushSnippet, Language

# Here you code..

lan = Language()
snippet = PushSnippet('t', 'd', 's', lan.swift)
res = snippet.push()

print(res)
