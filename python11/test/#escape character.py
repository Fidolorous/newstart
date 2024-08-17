#escape character

import re
x = 'We just received $10.00 for drugs.'
y = re.findall(r'\$[0-9.]+', x)

print(y)