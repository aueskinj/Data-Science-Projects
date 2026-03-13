import json
from faker import Faker
import os

# Configuration
FILE_NAME = "customers_500mb.json"
TARGET_SIZE_MB = 500
TARGET_SIZE_BYTES = TARGET_SIZE_MB * 1024 * 1024
fake = Faker()

def generate_customer():
    """Generates a single customer dictionary."""
    return {
        "id": fake.uuid4(),
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address().replace('\n', ', '),
        "phone": fake.phone_number(),
        "profile": {
            "job": fake.job(),
            "company": fake.company(),
            "birthdate": str(fake.date_of_birth()),
        },
        "account_created": str(fake.date_this_decade()),
    }

def create_large_json():
    print(f"Generating {FILE_NAME} (~{TARGET_SIZE_MB}MB)...")
    
    with open(FILE_NAME, "w") as f:
        f.write("[\n")  # Start JSON array
        
        first = True
        current_size = 0
        count = 0
        
        while current_size < TARGET_SIZE_BYTES:
            if not first:
                f.write(",\n")
            
            customer = generate_customer()
            json.dump(customer, f)
            
            first = False
            count += 1
            
            # Periodically check file size (faster than checking every iteration)
            if count % 100 == 0:
                current_size = os.path.getsize(FILE_NAME)
                print(f"\rCurrent size: {current_size / (1024*1024):.2f} MB", end="")

        f.write("\n]")  # Close JSON array
    print(f"\nDone. {count} customers generated.")

if __name__ == "__main__":
    # Install with: pip install faker
    create_large_json()

