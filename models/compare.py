from data.bread_products import products
from models.absorption import absorbable_nutrients

def compare():
    results = {}

    for name, product in products.items():
        results[name] = absorbable_nutrients(product)

    return results


# run comparison
results = compare()

for name, values in results.items():
    print("\n", name)
    print("Iron:", round(values["iron"], 2))
    print("Zinc:", round(values["zinc"], 2))
