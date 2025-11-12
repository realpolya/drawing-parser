# starting a drawing parser code

import re
from pdfminer.high_level import extract_pages, extract_text

# for page in extract_pages("./data/sample.pdf"):

#     for element in page:
#         print(element)

text = extract_text("./data/sample.pdf")
# print(text)

letter_pattern = re.compile(r"^[A-Z].*") # regex letter_pattern for an uppercase letter start of string
matches = letter_pattern.findall(text)
print(matches)

dimension_pattern = re.compile(r"^\d+\'-\d+\"$", re.MULTILINE)
dim_matches = dimension_pattern.findall(text)
print(dim_matches)

for m in dim_matches:
    print(m)