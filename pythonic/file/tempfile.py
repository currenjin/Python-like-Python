# tempfile

import tempfile

with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

with tempfile.NamedTemporaryFile(delete=False) as t:
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkdtemp()
print(temp_dir)
