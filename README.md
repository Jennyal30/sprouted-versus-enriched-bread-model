# sprouted-versus-enriched-bread-model
Bioavailability comparison of enriched bread versus sprouted grains using nutrient absorption modelling
# Sprouted vs Enriched Bread: Bioavailability Comparison Model

## Overview
This project models the impact of food processing on micronutrient bioavailability by comparing enriched bread formulations with sprouted grain systems.

It focuses on how anti-nutrient reduction (phytate degradation) affects absorbable iron and zinc levels.

---

## Research Question
How does grain processing (sprouting vs enrichment) influence micronutrient bioavailability under anti-nutrient constraints?

---

## Model Structure

### 1. Food Composition Layer
Defines nutrient and phytate profiles for:
- Enriched bread
- Sprouted grains
### 2. Processing Layer
Simulates food processing effects:
- Enrichment (no phytate reduction)
- Sprouting (reduced phytate levels)
### 3. Absorption Model
Applies a phytate inhibition function:
- Higher phytate → lower absorption
- Linear correction approximation

### 4. Comparative Analysis
Computes absorbable iron and zinc for both systems.

---

## Results

| Product            | Absorbable Iron | Absorbable Zinc |
|------------------|-----------------|----------------|
| Enriched Bread    | 3.2             | 1.8            |
| Sprouted Grains   | 5.8             | 2.9            |

---

## Key Insight
Sprouted grains show consistently higher bioavailable micronutrients due to reduced anti-nutrient content, despite similar or slightly higher baseline nutrient composition in enriched products.

---

## Scientific Relevance
This model reflects simplified dietary bioavailability assessment approaches used in:
- food systems modelling
- plant-based nutrition research
- dietary optimisation frameworks

--
## Limitations
- Simplified linear absorption model
- No enzymatic kinetics included
- Static phytate reduction assumptions

--
## Link to Broader Work
This project complements a larger bioavailability-aware modelling framework that extends nutrient analysis beyond intake-based metrics into absorbable nutrient estimation.

---

## Future Work
- integrate enzyme-driven phytate degradation kinetics
- expand to full meal-level optimisation
- incorporate multiple micronutrients simultaneously
