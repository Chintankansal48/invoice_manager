# Assignment

Instructions to run the assignment:

### 1. Clone the repository and install dependencies:
```
pip install -r requirements.txt
```

### 3. Run the server
```bash
python manage.py migrate
python manage.py runserver
```

### 5. Import the Postman Collection
With the server running at http://127.0.0.1:8000/, import the Postman collection to test the endpoints.

### Assumptions:
1. Unique Invoice Number: Each invoice has a unique invoice_number to distinguish it from others, ensuring easy tracking and no duplication.

2. Line Total Calculation: The line_total in each invoice detail must equal quantity * price to maintain data accuracy and prevent inconsistencies.

3. Minimum One Detail Entry: Every invoice requires at least one detail entry, as an invoice without items is considered invalid.