# AI Construction Intelligence — Armenia
Professional MVP for Armenian construction teams. Python/FastAPI, SQLAlchemy, SQLite/PostgreSQL, scikit-learn and a responsive dashboard.

## Features
- Indicative construction cost estimation in AMD
- Material catalog with supplier/city/unit fields
- Delay-risk probability model
- Budget optimization suggestions
- Rule-based project risk register
- Project CRUD, dashboard summary, API docs and tests

## Run
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
python scripts/seed_db.py
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000 and API docs at /docs. Run tests with `pytest -q`.

## Armenia data disclaimer
Seed prices and sample projects are **synthetic demonstration data**, not verified supplier quotations or live market feeds. Cost coefficients are indicative planning assumptions, not a bill of quantities or contractor quote. Replace with verified Armenian supplier offers and historical project records before commercial use. The ML model is trained on synthetic sample data and is not validated for operational decisions.

## Production checklist
Add real supplier integrations, authenticated role-based access, audit logs, database migrations, backups, HTTPS, monitoring, and model validation by qualified local construction estimators. Validate VAT/tax treatment, standards, labor rates and project-specific quantities.

## Stack
FastAPI · SQLAlchemy · PostgreSQL/SQLite · Pandas · NumPy · scikit-learn · HTML/CSS/JS · Pytest
