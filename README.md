# Marvel Rivals Hot List — Role-Standardized Hero Scores & Tier List (Season 6)

This project takes a scraped **Marvel Rivals Hot List (Season 6)** dataset and creates:

1. A **role-standardized** dataset that accounts for different numbers of heroes per role (which can inflate pick rates).
2. A **composite hero score** based on pick rate + win rate.
3. A **tier list** (S/A/B/C/D) generated from the hero score.

---

## What This Script Does

### 1) Load Data
Reads the Season 6 CSV:

- **Input:** `marvel_rivals_hot_list_season_6.csv`

### 2) Convert Percent Columns to Decimals
The dataset includes percent columns:

- `Pick Rate (%)` → `Pick Rate` as a decimal
- `Win Rate (%)` → `Win Rate` as a decimal

Example:
- `12.5%` becomes `0.125`

### 3) Standardize Pick Rate by Role
Pick rates can look “inflated” in roles with fewer heroes. To fix this, the script standardizes pick rate within each role.

It computes:

- **Role mean pick rate**
  - `role_mean_pick`: mean `Pick Rate` within each `Role`
- **Role-normalized pick rate**
  - `pick_norm = Pick Rate / role_mean_pick`
  - Interpretation:
    - `1.0` = average pick rate for that role
    - `>1.0` = above-average popularity for that role
    - `<1.0` = below-average popularity for that role
- **Within-role z-scores**
  - `pick_z`: pick rate z-score within each role
  - `win_z`: win rate z-score within each role  
  Z-score meaning:
  - `0` = average within role
  - `+1` = 1 standard deviation above role average
  - `-1` = 1 standard deviation below role average

### 4) Compute Hero Score
Creates a weighted composite score:

- `hero_score = 0.6 * pick_z + 0.4 * win_z`

Weights can be adjusted depending on whether you want the score to emphasize **meta popularity** (pick rate) or **performance** (win rate).

### 5) Export Standardized Dataset
Exports a clean dataset with the main metrics:

- **Output:** `marvel_rivals_standardized.csv`

Columns included:
- `Hero Name`, `Role`, `Rank`, `Pick Rate`, `Win Rate`
- `pick_norm`, `pick_z`, `win_z`, `hero_score`

### 6) Create Tier List
Assigns tiers using hero score thresholds:

| Tier | hero_score range |
|------|------------------|
| S    | ≥ 1.0            |
| A    | 0.3 to < 1.0     |
| B    | -0.3 to < 0.3    |
| C    | -1.0 to < -0.3   |
| D    | < -1.0           |

Exports a tier list CSV:

- **Output:** `marvel_rivals_tier_list.csv`

---

## Files

### Input
- `marvel_rivals_hot_list_season_6.csv`

Expected columns in the input CSV:
- `Hero Name`
- `Role`
- `Rank`
- `Pick Rate (%)`
- `Win Rate (%)`

### Outputs
- `marvel_rivals_standardized.csv`  
  Standardized metrics including z-scores and hero_score.

- `marvel_rivals_tier_list.csv`  
  Tier list output containing: `Hero Name`, `Role`, `Rank`, `Pick Rate`, `Win Rate`, `hero_score`, `tier`

---

## Requirements

Install dependencies:

```bash
pip install pandas numpy