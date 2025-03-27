import pandas as pd
from accounts.models import Flights
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings") 
django.setup()

def run():
    csv_file_path = "Clean_Dataset.csv"  

    # Read CSV file
    df = pd.read_csv(csv_file_path)

    # Required columns
    required_columns = [
        "airline", "flight", "source_city", "departure_time", "stops", 
        "arrival_time", "destination_city", "duration", "days_left", "price"
    ]
    
    # Check if all required columns exist
    if not all(col in df.columns for col in required_columns):
        missing_cols = [col for col in required_columns if col not in df.columns]
        raise ValueError(f"Missing columns in CSV: {missing_cols}")

    # Convert data types
    df["duration"] = pd.to_numeric(df["duration"], errors="coerce")
    df["days_left"] = pd.to_numeric(df["days_left"], errors="coerce", downcast="integer")
    df["price"] = pd.to_numeric(df["price"], errors="coerce", downcast="integer")

    # Drop invalid rows
    df = df.dropna()

    # Create list of Flight objects for bulk insertion
    flights_to_insert = [
        Flights(
            airline=row["airline"],
            flight=row["flight"],
            source_city=row["source_city"],
            departure_time=row["departure_time"],
            stops=row["stops"],
            arrival_time=row["arrival_time"],
            destination_city=row["destination_city"],
            duration=row["duration"],
            days_left=row["days_left"],
            price=row["price"]
        )
        for _, row in df.iterrows()
    ]

    # Bulk insert
    Flights.objects.bulk_create(flights_to_insert, batch_size=1000)  # Insert 1000 rows at a time

    print(f"{len(flights_to_insert)} records inserted successfully.")

