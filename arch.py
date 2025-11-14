# testing parsing architecture pdf drawings
# goals:
# understand scale and dimensions
# understand different line types (property line, dashed line, solid line, etc)
# understand multiple lines forming a shape (rectangle, polygon, etc)
# associate text with shapes
# calculate areas of shape
# calculate distances between shapes
# understand drawing orientation (North)
# test: can you calculate the distance between the property line and the proposed building? existing building?


import fitz
import PIL.Image
import io

# open file
pdf = fitz.open("./data/sample.pdf")
page = pdf[0]

# get vector geometry
vector_data = page.get_drawings()

# if a vector
if len(vector_data) > 0:

    # each shape in the drawing
    for shape in vector_data:

        print(shape)

        # for item in shape["items"]:

        #         # get lines
        #         if item[0] == "l":
        #             point1 = item[1]
        #             point2 = item[2]
        #             print("Line: ", point1, point2)
                
        #         # get curves
        #         if item[0] == "c":
        #             print("Curve:", item)


# what print(shape) gives us:
shape = {
    'items': [
        # rectangle-like shape
        ('qu', Quad(Point(2331.1499, 1664.1600),
                Point(2331.1499, 1603.9501),
                Point(2528.3398, 1664.1600),
                Point(2528.3398, 1603.9501)))
    ],
    'type': 's', # stroke only (outlined rectangle)
    'stroke_opacity': 1.0, # full opacity
    'color': (0.0, 0.0, 0.0), # black
    'width': 0.5699999928474426, # thickness in pdf, 1pt = 1/72 inch
    'lineCap': (1, 1, 1),
    'lineJoin': 0.029999999329447746,
    'closePath': False, # not a closed path, but its a quad (rectangle)
    'dashes': '[] 0', # this is a solid line
    'rect': Rect(2331.1499, 1603.9501, 2528.3398, 1664.1600), # bounding box
    'layer': '',
    'seqno': 1889, # drawing order, this was the 1889th thing to be completed
    'fill': None, # fill would be mentioned here
    'fill_opacity': None, # opacity would be mentioned here
    'even_odd': None #
}