import net


url = 'https://www.w3school.com.cn/tags/index.asp'
tables = net.Spider(url).find_tables(text_only=True)
table = tables[0]
for row in table:
    tag = row[0].text
    if tag.startswith('<') and tag.endswith('>'):
        tag = tag[1:len(tag)-1]
        if len(tag) > 1:
            c = tag[0].upper()
            tag = c + tag[1:]
            if not tag.startswith('!'):
                print("class %s(Element): pass" % tag)
