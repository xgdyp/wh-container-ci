import json
prefix = 'registry.cn-hangzhou.aliyuncs.com/whcr/'

d = {}
origin_trans_d = {}
with open('issue-content.md') as f:
    for line in f.readlines():
        origin = line.strip()
        ccnt = line.count('/')
        if ccnt == 2:
            parts = origin.split('/')
            part = parts[-2] + '/'+ parts[-1]
            print(part)
            origin_trans_d[origin] =part
        elif ccnt == 1 or ccnt == 0:
            origin_trans_d[origin] =origin

        # print(t)s
        # target = origin_trans_d[origin]
        target = origin_trans_d[origin].replace('/','.')
        target = prefix + target
        d[origin] = target
    # print(d)

output_file = 'images.json'

with open(output_file, 'w') as f:
    # 确保文件以UTF-8编码写入，这在处理特殊字符时很重要
    json.dump(d, f, indent=4, ensure_ascii=False)
