print ("""     
          ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
          ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
          ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
          ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
          ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
          ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝""")


print('hello, welcome to passwords manager')
a = input('enter space and then ur password:  ')
lis = [a]
spisok = lis

file = open('passwords.txt', 'a', encoding='utf-8')
file.write(a)
file.close()

print ('if u want to see urs passwords enter pass')
b = input()
if b == 'pass':
    file1 = open('passwords.txt', 'r', encoding='utf-8')
    content = file1.read()
    print (content)

else:
    print ('this command isnt available')