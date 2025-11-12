# starting a drawing parser code
# lesson taught here: https://www.youtube.com/watch?v=w2r2Bg42UPY

import re
from pdfminer.high_level import extract_pages, extract_text

'''Extract text with pdf miner'''
# for page in extract_pages("./data/sample.pdf"):

#     for element in page:
#         print(element)

# text = extract_text("./data/sample.pdf")
# # print(text)

# letter_pattern = re.compile(r"^[A-Z].*") # regex letter_pattern for an uppercase letter start of string
# matches = letter_pattern.findall(text)
# print(matches)

# dimension_pattern = re.compile(r"^\d+\'-\d+\"$", re.MULTILINE)
# dim_matches = dimension_pattern.findall(text)
# print(dim_matches)

# for m in dim_matches:
#     print(m)


'''Extract image PyMuPDF - https://pymupdf.readthedocs.io/en/latest/'''
import fitz
import PIL.Image
import io

# pdf = fitz.open("./data/hyatt.pdf")
# count = 1
# for i in range(len(pdf)):
#     # iterate over the pages
#     page = pdf[i]
#     images = page.get_images()
#     for image in images:
#         base_img = pdf.extract_image(image[0])
#         image_data = base_img["image"]
#         img = PIL.Image.open(io.BytesIO(image_data))
#         extension = base_img["ext"]
#         img.save(open(f"image{count}.{extension}", "wb"))
#         count += 1

# understand whether the file is a vector
pdf = fitz.open("./data/sample.pdf")
page = pdf[0]


vector_data = page.get_drawings()

# array of all vector shapes
# len > 0: vector shapes
# len == 0: pdf is an image, no vectors
print("The number of vectors in the drawings: ", len(vector_data))