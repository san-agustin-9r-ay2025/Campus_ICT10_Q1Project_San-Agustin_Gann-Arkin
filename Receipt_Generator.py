# Receipt Generator

from pyscript import document, display

# make function
def calculating(e):
    # make variables connected to ID's
    prod1 = document.getElementById('snare')
    prod2 = document.getElementById('bass')
    prod3 = document.getElementById('cymbals1')
    prod4 = document.getElementById('cymbals2')
    prod5 = document.getElementById('cymbals3')
    prod6 = document.getElementById('tom3')
    prod7 = document.getElementById('tom1')
    prod8 = document.getElementById('tom2')
    prod9 = document.getElementById('stool')
    prod10 = document.getElementById('drum_sticks')

    # calculation
    subtotal = (float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked + float(prod5.value) * prod5.checked + float(prod6.value) * prod6.checked + float(prod7.value) * prod7.checked + float(prod8.value) * prod8.checked + float(prod9.value) * prod9.checked + float(prod1.value) * prod1.checked + float(prod10.value) * prod10.checked)

    # result of calculation
    Total_amount = subtotal * .12

    # print on website
    display( f'Receipt Generator: {Total_amount} Pesos', target='output')

