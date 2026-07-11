# ESPN-WebScraping

ESPN college football web scraper and Jupyter analytics — Selenium pipeline for player/team stats plus Pandas/Seaborn visualizations.

Built for a Fall 2023 Data & Visual Analytics course.

---

## Components

### 1. Scraping pipeline (`updateData/`)

Selenium scripts that scrape ESPN for:
- Player stats (passing, rushing, receiving, defense)
- Weekly game data (week 0–14)

```bash
cd updateData
python main.py
```

### 2. Analysis notebook (`ESPN.football.ipynb`)

Pandas/Seaborn/Matplotlib visualizations — e.g., defensive tackle distributions across schools (OSU, UGA, GAST, LSU).

```bash
jupyter notebook ESPN.football.ipynb
```

Pre-scraped data is included in `data/` (week0–week14 CSVs plus season stat CSVs).

---

## Tech stack

- Python 3.8+
- Selenium WebDriver (Chrome)
- Pandas, NumPy, Matplotlib, Seaborn
- Jupyter Notebook

---

## Quick start

```bash
git clone https://github.com/Kaireega/ESPN-WebScraping.git
cd ESPN-WebScraping
pip install -r requirements.txt
```

**Prerequisites:** Chrome browser. Selenium Manager handles ChromeDriver automatically on modern Selenium versions.

To scrape fresh data, edit `updateData/setDriver.py` if needed for your ChromeDriver path, then:

```bash
cd updateData
python main.py
```

---

## Data files

| File | Description |
|------|-------------|
| `data/passing.csv` | Season passing stats |
| `data/rushing.csv` | Season rushing stats |
| `data/receiving.csv` | Season receiving stats |
| `data/defense.csv` | Season defensive stats |
| `data/week0.csv` … `week14.csv` | Weekly game data |

---

## Author

**Kai'ree Gay** — [GitHub](https://github.com/Kaireega)
