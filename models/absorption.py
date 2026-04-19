# Bioavailability model for bread systems

def absorbable_nutrients(product):
    phytate = product["phytate"]

    # simple inhibition function
    factor = 1 - (0.25 * phytate)

    if factor < 0:
        factor = 0

    return {
        "iron": product["iron"] * factor,
        "zinc": product["zinc"] * factor
    }
