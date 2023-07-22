import re
highlight_keywords = open('media\keywords.txt' ,'r', encoding = 'utf-8')
s1 = " ".join([i for i in highlight_keywords])
phrases_keyword=[]
for i in s1.split('\n '):
    phrases_keyword.append(i)

#---------------------------
list = ["Sun Microsystems","Script","java","Java","Applets","applets","Applet","java applet","Machine code","Application","JVM","Jvm","jvm","Client Side",
        "java virual machine","java Virual Machine","C++","byte code","Byte-code","Byte code","java Run-time","JavaScript","Java Script","Netscape",
        "DHTML","Dynamic Hyper Text Markup","HTML","Object Oriented programming","J2SE","J2ME","J2EE","Java SE","Java EE","Java ME",
        "Java Standard Edition","Java Enterprise Edition","Java Micro Edition","Platform Independent","Machine Code","JDK","Java Development Kit","OOP","Class Library","JSP","javaBeans",
        "Java Server Pages","Simple","Object-Oriented","Distributed","Interpreted","Robust","Secure","Architecture Neutral","Portable","Multithreaded","Dynamic",
        "Javac","Applet Viewer","NetBeans","Eclipse","IntelliJ","BlueJ","أنظمة التشغيل","الجافا",
        "الجافا ابلت","لغة ترميز النص الفائق الديناميكية","التلفزيون التفاعلي",
        "آلة الجافا الافتراضية"]

def highlight(content):
    for i , x in zip(list,phrases_keyword):
        if i in content:
            content = content.replace(i, '<mark>{}</mark>'.format(i))
        if x in content:
            content = content.replace(x, '<mark style="background-color:#d0ecfd;">{}</mark>'.format(x))
    return content
   

