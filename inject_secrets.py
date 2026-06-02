import os

key = os.environ['JSONBIN_API_KEY']
pin = os.environ['ADMIN_PIN']

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace('__JSONBIN_API_KEY__', key)
content = content.replace('__ADMIN_PIN__', pin)

with open('index.html', 'w') as f:
    f.write(content)

print(f'Injected API key (prefix: {key[:8]}...) and PIN')
