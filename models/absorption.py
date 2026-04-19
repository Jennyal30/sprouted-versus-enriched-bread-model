# Bioavailability model (post-processing)

def absorbable_nutrients(product):
    phytate = product["phytate"]

    factor = 1 - (0.25 * phytate)
    if factor < 0:
        factor = 0

    return {
        "iron": product["iron"] * factor,
        "zinc": product["zinc"] * factor
    }
