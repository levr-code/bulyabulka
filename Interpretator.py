def Thebulka(file: str):
    #string buckweed flour
    #integer wheat flour
    def error(err, msg, line=None):
        print(f"{err} (Line {line+1}): {msg}")
        import os
        os._exit(0)
    def run(src, n, vars):
        for i in range(len(src)):
            i1=src[i]
            if len(i1)>0:
                if "<bulk>"in i1:
                    i1=i1.replace(f"<bulk>",str(input()))
                if "<buluka>"in i1:
                    i1=i1.replace(f"<buluka>",n)
                if '#' in i1:
                    i1 = i1.split('#')[0]
                if "<random>" in i1:
                    try:
                        i1=i1.replace(f"<random>",str(randint(0,10000)/10000))
                    except BaseException:
                        error("MixerError")
                for j in vars:
                    i1=i1.replace(f"<{j}>",str(vars[j]))
                if i1[:4]=="+bul":
                    try:
                        n=ord(n)
                        n+=i1.count("*bul*")
                        n+=i1.count("*bull*")*5
                        n+=i1.count("*buluma*")*10
                        n+=i1.count("*bulbul*")*100
                        n=chr(n)
                    except Exception:
                        error("ToManyIngredientError","+bul is working only with one",i)
                elif i1[:4]=="-bul":
                    try:
                        n=ord(n)
                        n-=i1.count("*bul*")
                        n-=i1.count("*bull*")*5
                        n-=i1.count("*buluma*")*10
                        n-=i1.count("*bulbul*")*100
                        n=chr(n)
                    except Exception:
                        error("ToManyIngredientError","-bul is working only with one",i)
                elif i1[:3]=='mya':
                    n+=(" ".join(i1[3:].split()))
                elif i1[:3]=='mac':
                    c=" ".join(i1[3:].split()[1:])
                    if i1[3:].split()[0] in vars:
                        vars[i1[3:].split()[0]]=c
                    else:
                        vars.setdefault(i1[3:].split()[0],c)
                elif i1[:5]=="bulka":
                    try:
                        try:
                            a=ord(n)>0
                        except:
                            a=True
                        if a:
                            print(n,end='')
                        else:
                            print("\n",end='')
                    except:
                        error("CrumbInThroatError","it's stuck",i)
                elif i1[:5]=="?lub?":
                    try:
                        if i1[6:].split(":")[1]=="=":
                            while i1[6:].split(":")[0]==i1[6:].split(":")[2][:-1]:
                                k=i+1
                                s1=[]
                                while src[k][:4]=="    ":
                                    s1.append(src[k][4:])
                                    k+=1
                                run(s1,n,vars)
                        if i1[6:].split(":")[1]=="!=":
                            while i1[6:].split(":")[0]!=i1[6:].split(":")[2][:-1]:
                                k=i+1
                                s1=[]
                                while src[k][:4]=="    ":
                                    s1.append(src[k][4:])
                                    k+=1
                                run(s1,n,vars)
                        if i1[6:].split(":")[1]==">":
                            while int(i1[6:].split(":")[0])>int(i1[6:].split(":")[2][:-1]):
                                k=i+1
                                s1=[]
                                while src[k][:4]=="    ":
                                    s1.append(src[k][4:])
                                    k+=1
                                run(s1,n,vars)
                        if i1[6:].split(":")[1]=="<":
                            while int(i1[6:].split(":")[0])<int(i1[6:].split(":")[2][:-1]):
                                k=i+1
                                s1=[]
                                while src[k][:4]=="    ":
                                    s1.append(src[k][4:])
                                    k+=1
                                run(s1,n,vars)
                        if i1[6:].split(":")[1]==">=":
                            while int(i1[6:].split(":")[0])>=int(i1[6:].split(":")[2][:-1]):
                                k=i+1
                                s1=[]
                                while src[k][:4]=="    ":
                                    s1.append(src[k][4:])
                                    k+=1
                                run(s1,n,vars)
                        if i1[6:].split(":")[1]=="<=":
                            while int(i1[6:].split(":")[0])<=int(i1[6:].split(":")[2][:-1]):
                                k=i+1
                                s1=[]
                                while src[k][:4]=="    ":
                                    s1.append(src[k][4:])
                                    k+=1
                                run(s1,n,vars)
                    except:
                        error("RecipeLieError","why would you put cucumbers there?")
                elif i1[:5]=="?bul?":
                    try:
                        if i1[6:].split(":")[1]=="=":
                            if i1[6:].split(":")[0]==i1[6:].split(":")[2][:-1]:
                                k=i+1
                                s1=[]
                                while src[k][:4]=="    ":
                                    s1.append(src[k][4:])
                                    k+=1
                                run(s1,n,vars)
                        if i1[6:].split(":")[1]=="!=":
                            if i1[6:].split(":")[0]!=i1[6:].split(":")[2][:-1]:
                                k=i+1
                                s1=[]
                                while src[k][:4]=="    ":
                                    s1.append(src[k][4:])
                                    k+=1
                                run(s1,n,vars)
                        if i1[6:].split(":")[1]==">":
                            if float(i1[6:].split(":")[0])>float(i1[6:].split(":")[2][:-1]):
                                k=i+1
                                s1=[]
                                while src[k][:4]=="    ":
                                    s1.append(src[k][4:])
                                    k+=1
                                run(s1,n,vars)
                        if i1[6:].split(":")[1]=="<":
                            if float(i1[6:].split(":")[0])<float(i1[6:].split(":")[2][:-1]):
                                k=i+1
                                s1=[]
                                while src[k][:4]=="    ":
                                    s1.append(src[k][4:])
                                    k+=1
                                run(s1,n,vars)
                        if i1[6:].split(":")[1]==">=":
                            if float(i1[6:].split(":")[0])>=float(i1[6:].split(":")[2][:-1]):
                                k=i+1
                                s1=[]
                                while src[k][:4]=="    ":
                                    s1.append(src[k][4:])
                                    k+=1
                                run(s1,n,vars)
                        if i1[6:].split(":")[1]=="<=":
                            if float(i1[6:].split(":")[0])<=float(i1[6:].split(":")[2][:-1]):
                                k=i+1
                                s1=[]
                                while src[k][:4]=="    ":
                                    s1.append(src[k][4:])
                                    k+=1
                                run(s1,n,vars)
                    except:
                        error()
                elif i1[:5]=="/bul/":
                    k=i+1
                    s1=[]
                    while src[k][:4]=="    ":
                        s1.append(src[k][4:])
                        k+=1
                    for i in range(int(float(i1[6:].split(":")[0]))):
                            run([j.replace("<myau>",str(i)) for j in s1],n,vars)
                elif i1[:5]=="bulya":
                    n=chr(0)
                elif i1[:5]=="/bulr":
                    try:
                        vars[i1[6:].split()[0]]=randint(int(i1[6:].split()[1]),int(i1[6:].split()[2]))
                    except BaseException as e:
                        error("MixingError","mixer broke and unable to mix",i)
                def addtochat(c):
                    if "math" in vars:
                        vars["math"]=c
                    else:
                        vars.setdefault("math",c)
                a=i1
                try:
                    if  a[:5]=="/bulu":
                        addtochat(float(a[6:].split()[0])+float(a[6:].split()[1]))
                    elif a[:4]=="/blu":
                        addtochat(float(a[5:].split()[0])-float(a[5:].split()[1]))
                    elif a[:4]=="/bul" and not a[4]=="/":
                        addtochat(float(a[5:].split()[0])*float(a[5:].split()[1]))
                    elif a[:4]=="/lub":
                        addtochat(float(a[5:].split()[0])/float(a[5:].split()[1]))
                    elif a[:4]=="/lbu":
                        addtochat(float(a[5:].split()[0])%float(a[5:].split()[1]))
                except ZeroDivisionError:
                    error("ColdOvenError","oven is cold how will you bake?",i)
                except TypeError:
                    error("WrongFlourError","buckwheat flour is not working here, your bulka is to hard",i)
