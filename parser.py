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

if len(vector_data) > 0:
    for shape in vector_data:

        # print(shape)

        for item in shape["items"]:

            if item[0] == "l":
                point1 = item[1]
                point2 = item[2]
                print("Line: ", point1, point2)
            
            if item[0] == "c":
                print("Curve:", item)


text = page.get_text("dict")

for block in text["blocks"]:
    if block["type"] == 0:
        for line in block["lines"]:
            for span in line["spans"]:
                print(span["text"], span["bbox"])


# save PDF as a png
pix = page.get_pixmap(dpi=300) # dpi 
# pix.save("page.png")


# visualize the extracted
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
for s in vector_data:
    for item in s["items"]:
        if item[0] == "l":
            x0, y0 = item[1]
            x1, y1 = item[2]
            ax.plot([x0, x1], [y0, y1], color='black')

plt.gca().invert_yaxis()
plt.show()