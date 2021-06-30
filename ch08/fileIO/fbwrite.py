#binary file: sound, img

with open('data.bin', 'wb') as f:
    text='날씨가 덥다'
    f.write(text.encode())

with open('data.bin', 'rb') as f:
    data=f.read()
    text=data.decode()
    print(text)