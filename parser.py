# starting a drawing parser code

import re
from pdfminer.high_level import extract_pages, extract_text

# for page in extract_pages("./data/sample.pdf"):

#     for element in page:
#         print(element)

text = extract_text("./data/sample.pdf")
# print(text)

pattern = re.compile(r"^[A-Z].*") # regex pattern for an uppercase letter start of string
matches = pattern.findall(text)
print(matches)