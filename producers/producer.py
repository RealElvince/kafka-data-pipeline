from faker import Faker
import json
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
    bootstrap_servers='localhost:9092',
    value_serializer = lambda data: json.dumps(data).encode('utf-8')
                         
)