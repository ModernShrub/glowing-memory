import matplotlib.pyplot as plt
import speedtest
import time

lds=[]
lus=[]

x=[1,2,3,4,5]

for i in x :
    st = speedtest.Speedtest()
    dos = round(st.download()/1000000,2)
    ups = round(st.upload()/1000000,2)
    lds.append(dos)
    lus.append(ups)
    time.sleep(60)
    print(lds)
    print(lus)
    if i == 5:
        break
    
plt.figure(figsize=(15,7))
plt.title("Speed")
plt.plot(x,lds,label="Download Speed")
plt.plot(x,lus,label="Upload Speed")
plt.legend()
plt.show()
    