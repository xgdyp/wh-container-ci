import json
import re

prefix = 'registry.cn-hangzhou.aliyuncs.com/whcr/hf'
project_name = ""
d = {}
origin_trans_d = {}
with open('issue-content.md') as f:
    for line in f.readlines():
        origin = line.strip()
        if "::project:" in origin :
            # process project name
            project_name = origin.strip('::project:').strip()
        else:
            ccnt = line.count('/')
            if ccnt == 2:
                parts = origin.split('/')
                part = parts[-2] + '/'+ parts[-1]
                print(part)
                origin_trans_d[origin] =part
            elif ccnt == 1 or ccnt == 0:
                origin_trans_d[origin] =origin

                print('here')
                print(origin)
            # target = origin_trans_d[origin]
            # separators = r"[/:]"
            
            target = origin_trans_d[origin].replace('registry.hf.space/','').replace('/','--').replace(':','--').replace('.','--')


            target = prefix +project_name +':' + target
            print(target)
            d[origin] = target
    # print(d)
if "" in d:
    del d[""]
output_file = 'images.json'

with open(output_file, 'w') as f:
    # 确保文件以UTF-8编码写入，这在处理特殊字符时很重要
    json.dump(d, f, indent=4, ensure_ascii=False)

import json

with open('images.json','r') as f:
    
  images = json.load(f)


prompt = "docker pull {} && docker tag {} {} \n"

rst_lst = []
for origin, trans in images.items():

  if "--" not in trans:
    break

  dnum = trans.count('--')
  trans = trans.replace("registry.cn-hangzhou.aliyuncs.com/whcr/","IP.IP.IP.IP/project/")
  rst = prompt.format(trans, trans, origin)
  rst_lst.append(rst)

with open('issue-feedback.md', 'w') as f:
  for _ in rst_lst:
    f.write(_)

  
print('finished')
