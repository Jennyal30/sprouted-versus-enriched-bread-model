from data.bread_products import products
from models.processing import apply_processing
from models.absorption import absorbable_nutrients

def run_comparison():

    for name, product in products.items():

        # apply processing logic
        if name == "sprouted_grains":
            processed = apply_processing(product, "sprouted")
        else:
            processed = apply_processing(product, "enriched")

        result = absorbable_nutrients(processed)

        print("\nProduct:", name)
        print("Absorbable Iron:", round(result["iron"], 2))
        print("Absorbable Zinc:", round(result["zinc"], 2))


run_comparison()
