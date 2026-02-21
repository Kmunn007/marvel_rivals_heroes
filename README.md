# Marvel Rivals --- Hero Pick-Rate & Win-Rate Analysis

This project analyzes **Marvel Rivals heroes** using:

-   **Hero name**
-   **Pick rate**
-   **Win rate**
-   **Platform** (PC / Console)
-   **Rank brackets** (Bronze → Grandmaster)

The goal is to understand:

-   which heroes are **popular AND strong**,\
-   which heroes are **over-picked but under-performing**,\
-   and which heroes are **underrated sleepers** that win more than
    they're played.

The project is written in **Python** using **Pandas** for data analysis
and (optionally) Matplotlib for visualizations.

------------------------------------------------------------------------

## 📂 Dataset

Your main CSV is expected to look like:

  Hero     Platform   Rank       Pick Rate   Win Rate   Game Mode     Role
  -------- ---------- ---------- ----------- ---------- ------------- ----------
  Angela   PC         Bronze     0.0684      0.5282     Competitive   Vanguard
  Hulk     PC         Platinum   0.113       0.541      Competitive   Vanguard
  Storm    PC         Bronze     0.0135      0.5422     Competitive   Duelist

> Pick/Win rates are decimals (e.g., `0.52 = 52%`).

File name:

    hero_stats.csv

Place it in the same folder as `analysis.py`.

------------------------------------------------------------------------

## 🚀 Features

### ✔️ Sort heroes by platform → rank → win rate

Organizes meta trends clearly across ladders and devices.

### ✔️ Pick-rate vs Win-rate comparison

Identifies:

-   🟢 **Meta monsters** (high pick, high win)\
-   🔵 **Underrated heroes** (low pick, high win)\
-   🟡 **Over-picked but weak**\
-   🔴 **Low pick & low win**

### ✔️ Outlier-aware classification

Uses **median** by default (robust to skewed data), but supports
**mean** if preferred.

### ✔️ Optional scatter plot visualization

Visualizes hero power vs popularity.

------------------------------------------------------------------------

## 🛠️ Installation

### 1️⃣ Clone the repo

``` bash
git clone https://github.com/<your-username>/marvel-rivals-analysis.git
cd marvel-rivals-analysis
```

### 2️⃣ Create / activate environment (Anaconda example)

``` bash
conda create -n dev python=3.11
conda activate dev
```

### 3️⃣ Install dependencies

``` bash
pip install pandas matplotlib
```

------------------------------------------------------------------------

## ▶️ Running the analysis

Run the script:

``` bash
python analysis.py
```

You should see output such as:

    Top by win rate (organized):
    Rocket Raccoon ... 0.5705
    Peni Parker ...    0.5678
    Magik ...

------------------------------------------------------------------------

## 📊 Pick-Rate vs Win-Rate Insights

The script highlights:

### Over-picked but under-performing

Players select them a lot --- but lose:

``` python
overpicked = df[
    (df["Pick Rate"] > df["Pick Rate"].median()) &
    (df["Win Rate"] < df["Win Rate"].median())
]
```

### Underrated strong heroes

Low play, high success:

``` python
underrated = df[
    (df["Pick Rate"] < df["Pick Rate"].median()) &
    (df["Win Rate"] > df["Win Rate"].median())
]
```

You can switch to **mean** if desired by replacing `.median()` with
`.mean()`.

------------------------------------------------------------------------

## 📈 Visualization (optional)

Run to visualize pick vs win:

``` python
plt.scatter(df["Pick Rate"], df["Win Rate"])
...
plt.show()
```

This helps spot:

-   top-right = meta,
-   top-left = sleepers,
-   bottom-right = overrated,
-   bottom-left = weak.

------------------------------------------------------------------------

## 🔮 Future ideas

-   pull stats automatically from APIs / web scraping\
-   role-based comparisons\
-   patch-to-patch balance tracking\
-   dashboard (Streamlit)

------------------------------------------------------------------------

## 🤝 Contributing

PRs and suggestions welcome!

------------------------------------------------------------------------

## 📜 License

MIT --- feel free to use, modify, and build on this.
