import subprocess
import io

sp = subprocess.Popen(['date'], stdout=subprocess.PIPE, shell=True)
out = io.TextIOWrapper(sp.stdout, encoding='cp866')
s = ' ';
while s:
    s = out.readline()
    print(s)
