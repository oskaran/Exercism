import re

def parse(m):
    m = re.sub(r'__(.*)__', r'<strong>\1</strong>', m)
    m = re.sub(r'_(.*)_', r'<em>\1</em>', m)
    m = re.sub(r'^([^#*].*)', r'<p>\1</p>', m, flags=re.MULTILINE)
    m = re.sub(r'^\* (.*)', r'<li>\1</li>', m, flags=re.MULTILINE)
    m = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', m, flags=re.DOTALL)

    if (mo := re.match(r'^(#){1,6} ', m)):
        num_sharp = str(mo.group().count('#'))
        m = re.sub(r'^(#){1,6} (.*)', fr'<h{num_sharp}>\2</h{num_sharp}>', m, flags=re.MULTILINE)

    return m.replace('\n', '')
