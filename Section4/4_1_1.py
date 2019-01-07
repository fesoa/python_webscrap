# 데이터를 다루기 위한 바이너리/텍스트파일 쓰고 읽기

import sys
import io
import pickle # 객체나 텍스트를 직렬화, 역직렬화

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

bfilename = 'c:/Workflow/Webcrawling/Section4/test.bin'
tfilename = 'c:/Workflow/Webcrawling/Section4/test.txt'

data1 = 77
data2 = "Hello World!"
data3 = {"Apple","Mandarin","Orange"}

# 바이너리 쓰기
with open(bfilename, 'wb') as f: #binary로 쓰겠다
    pickle.dump(data1,f) # dumps: 객체를 바이너리로 쓸 때/ dumps: 문자열 직렬화
    pickle.dump(data2,f)
    pickle.dump(data3,f)

# 텍스트 쓰기
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))
