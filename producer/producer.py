from faker import Faker
import json
import time
from kafka import KafkaProducer




fake = Faker()

def get_registered_user():
    """Generate a fake registered user."""
    return {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.address(),
        "phone_number": fake.phone_number(),
        "created_at":fake.year()
    }


producer = KafkaProducer(
    bootstrap_servers=['localhost:9094'],
    value_serializer = lambda data: json.dumps(data).encode('utf-8')
                         
)


if __name__ == "__main__":
    while True:
        registered_data = get_registered_user()
        print(registered_data)
        producer.send("user-registered", value=registered_data)
        time.sleep(3)