from subprocess import call

content = '''\
#! /bin/bash
mv ./dummy_script.py ./temp 
touch ./script
echo "Hello" > ./script
cat script
'''

with open ('./run.sh', 'w') as rsh:
    rsh.write(content)

rc = call(content, shell=True)
