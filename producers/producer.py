from faker import Faker





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

    