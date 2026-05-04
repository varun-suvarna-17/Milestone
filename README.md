# Milestone 1 - Data Analytics Project

A data processing and analytics package that processes user activity events, applies transformations, and performs SQL-based analysis.

## Project Structure

```
├── funtionality.py          # Core data processing functions
├── queries.sql              # SQL queries for database analysis
└── analytics/               # Main package
    ├── main.py              # Entry point for analytics pipeline
    ├── data.py              # Sample data source
    ├── processor.py         # Data filtering functions
    ├── tasks.py             # Data transformation functions
    └── utils/
        ├── helper.py        # Utility functions (type conversion)
        └── __init__.py      # Package initializer
```

## Features

- **Data Filtering**: Extract specific event types (e.g., purchases) from raw data
- **Data Transformation**: Convert amounts to float, apply discounts (10%), add custom transformations
- **Higher-Order Functions**: Apply custom functions to data collections
- **SQL Analytics**: Window functions for ranking, counting, and analyzing user activity
- **Error Handling**: Robust exception handling with try-except blocks

## Running the Project

```bash
python analytics/main.py
```

## What It Does

1. Loads user activity data (logins and purchases)
2. Filters purchase events
3. Extracts and processes amounts
4. Applies discount calculations
5. Applies custom transformations using higher-order functions
6. Outputs results to console

## Output

- List of all purchases
- Processed amounts with type conversion
- Discounted amounts (90% of original)
- Amounts after custom transformations

## Data

Sample dataset includes user activities with:
- User IDs
- Event types (login, purchase)
- Transaction amounts
- Event timestamps

---

**Status**: Milestone 1 Assignment
