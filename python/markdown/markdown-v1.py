import re

def parse1(markdown):
    # re.sub(" ", s, flag = re.M | re.S)
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'
        m = re.match(r'\* (.*)', i)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res

#%%
def parse(m):
    #m = re.sub(r'__([^\n]+)__', r'<strong>\1</strong>', m)
    m = re.sub(r'__(.*)__', r'<strong>\1</strong>', m)
    #m = re.sub(r'_([^\n]+)_', r'<em>\1</em>', m)
    m = re.sub(r'_(.*)_', r'<em>\1</em>', m)

    m = re.sub(r'^([^#*].*)', r'<p>\1</p>', m, flags=re.MULTILINE)

    m = re.sub(r'^\* (.*)', r'<li>\1</li>', m, flags=re.MULTILINE)
    m = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', m, flags=re.DOTALL)
    # re.match(r'^(#){1,6}', e).group()
    # if (mo := re.match(r'^(#){1,6}', g)) != None:
    #m = re.sub(r'^([^#<].*)', r'<p>\1</p>', m, flags=re.MULTILINE)

    if (mo := re.match(r'^(#){1,6} ', m)): #, flags=re.MULTILINE
        num_sharp = str(mo.group().count('#'))
        #m = m.replace(mo.group(), '').join([f'<h{num_sharp}>', f'<h/{num_sharp}>'])
        m = re.sub(r'^(#){1,6} (.*)', fr'<h{num_sharp}>\2</h{num_sharp}>', m, flags=re.MULTILINE)

    m = m.replace('\n', '')

    return m
#%%

"""
• The ? matches zero or one of the preceding group.
• The * matches zero or more of the preceding group.
• The + matches one or more of the preceding group.
• [abc] matches any character between the brackets (such as a, b, or c).
"""
a = "This will be a paragraph" # "<p>This will be a paragraph</p>"
b = "_This will be italic_" # "<p><em>This will be italic</em></p>"
c = "__This will be bold__" # "<p><strong>This will be bold</strong></p>"
d = "This will _be_ __mixed__" # "<p>This will <em>be</em> <strong>mixed</strong></p>",
e = "# This will be an h1" # "<h1>This will be an h1</h1>")
f = "## This will be an h2" # "<h2>This will be an h2</h2>")
g = "###### This will be an h6" # "<h6>This will be an h6</h6>"
h = "* Item 1\n* Item 2" # "<ul><li>Item 1</li><li>Item 2</li></ul>"
k = "# Header!\n* __Bold Item__\n* _Italic Item_"
#"<h1>Header!</h1><ul><li><strong>Bold Item</strong></li><li><em>Italic Item</em></li></ul>",
l = "# This is a header with # and * in the text"
            #"<h1>This is a header with # and * in the text</h1>",
m = "* Item 1 with a # in the text\n* Item 2 with * in the text"
            #"<ul><li>Item 1 with a # in the text</li><li>Item 2 with * in the text</li></ul>",
n = "This is a paragraph with # and * in the text"
            #"<p>This is a paragraph with # and * in the text</p>",
o = "# Start a list\n* Item 1\n* Item 2\nEnd a list"
            # "<h1>Start a list</h1><ul><li>Item 1</li><li>Item 2</li></ul><p>End a list</p>",
