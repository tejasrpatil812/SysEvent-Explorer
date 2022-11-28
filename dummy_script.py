from subprocess import call

content = '''\
#! /bin/bash
touch ./script
echo "Hello" > ./script
cat script
'''

with open ('./run.sh', 'w') as rsh:
    rsh.write(content)

rc = call(content, shell=True)
rc = call('./run.sh', shell=True)
