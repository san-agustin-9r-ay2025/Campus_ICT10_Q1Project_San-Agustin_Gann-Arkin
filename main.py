# SKU Generator

from pyscript import document, display

# make function
def generatingSKU(e):
    # make variables connected to ID's
    typesChosen = document.getElementById('types').value
    productName = document.getElementById('product').value
    quantity = document.getElementById('stock').value

    # use examples for exercise 4: len, indexing/offset, converting to string form integer or float, .replace, .upper
    category = (typesChosen.upper()[0:4])
    length = str(len(productName))
    prodName = str(productName[0:2])
    numberQuantity = str(quantity.replace('1', 'a').replace('2', 'b').replace('3', 'c').replace('4', 'd').replace('5', 'e').replace('6', 'f').replace('7', 'g').replace('8', 'h').replace('9', 'i'))

    # combining resulting strings into one string
    SKU = (category + length + prodName + numberQuantity)

    # print on website
    display (f'SKU Generator: {SKU}', target='output')


