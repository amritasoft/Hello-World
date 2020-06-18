# import subprocess

# bash_com = "curl -s http://$HUB_HOST:4444/wd/hub/status | jq -r .value.ready "

# output=subprocess.Popen(bash_com, stdout=subprocess.PIPE)
# stdout = output.communicate()[0]
# print('STDOUT:{}'.format(stdout))

#  
import subprocess
out = subprocess.Popen(["curl", "-s", "http://localhost:4444/wd/hub/status","|","jq", ".value.ready"],encoding="utf-8",stdout = subprocess.PIPE, 
stderr = subprocess.STDOUT,shell=True)
stddata = out.communicate()[0].strip()

print(stddata)