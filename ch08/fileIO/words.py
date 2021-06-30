#영단어 저장
f=open('words.txt','a')
word=['sky','sea','earth','moon','tree','flower','grape','s','g','p']
for i in word:
    f.write(i+' ')

f.close()