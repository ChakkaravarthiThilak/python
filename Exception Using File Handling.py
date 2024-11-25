try:
    f=open("C:/Users/csc/Desktop/thilak.txt")
    try:
       f.write("Hello")
    except:
       print("Can't Write")
    finally:
       f.close()
except:
    print("Can't open")
