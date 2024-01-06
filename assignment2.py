def read(path):
    f=open(path,'r')
    d=f.read()
    f.close()
    return d
def filtered(data):
    lines=data.split('\n')
    r1=[]
    r2=[]
    for e in lines:
        if "sshd" in e:
            r1.append(e)
        elif "ftpd" in e:
            r2.append(e)
    return r1,r2
def writing(path1,q1):
    f1=open(path1,'w')
    for i in q1:
        f1.write(i+"\n")
    f1.close()
    return f1
text=read('linux_system_jun.log')
t=read('linux_system_july.log')
res1,res2=filtered(text)
result1,result2=filtered(t)
writing('system_sshd.log',res1+result1)
writing('system_fttp.log',res2+result2)
print(f'The total log lines generated for the service(daemon) "sshd" was "{len(res1+result1)}" lines.')
print(f'The total log lines generated for the service(daemon) "ftpd" was "{len(res2+result2)}" lines.')




            

