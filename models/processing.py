# Bread processing effects on phytate

def apply_processing(product, method="enriched"):
    """
    Simulates processing effects:
    - enriched bread: no phytate reduction
    - sprouted grains: reduced phytate
    - fermented bread: strongest reduction
    """

    phytate = product["phytate"]

    if method == "enriched":
        phytate *= 1.0
    elif method == "sprouted":
        phytate *= 0.5
    elif method == "fermented":
        phytate *= 0.4

    return {
        **product,
        "phytate": phytate
    }
