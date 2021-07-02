#beautifulSoup module

from bs4 import BeautifulSoup

html_str='''
<html>
<body>
    <ul class='item'>
        <li>인공지능</li>
        <li>b</li>
        <li>a</li>
    </ul>
</body>
</html>
'''
soup=BeautifulSoup(html_str,'html.parser')

ul=soup.find('ul')
#print(ul)
print(ul.text)