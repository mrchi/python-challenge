# coding=utf-8

from xmlrpc.client import ServerProxy


url = "http://www.pythonchallenge.com/pc/phonebook.php"
evil = "Bert"

with ServerProxy(url) as proxy:
    print(proxy.system.listMethods())
    print(proxy.system.methodHelp("phone"))
    print(proxy.phone(evil))

answer = "italy"
print(f"http://www.pythonchallenge.com/pc/return/{answer}.html")
