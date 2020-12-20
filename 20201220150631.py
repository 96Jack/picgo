import base64

with open('右.jpg', 'rb') as f:
    ls_f = base64.b64encode(f.read())
print(ls_f)
