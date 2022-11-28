with open ('./run.sh', 'w') as rsh:
    rsh.write('''\
#! /bin/bash
touch ./script
echo "Hello" > ./script
cat script
mv script dummy
''')
