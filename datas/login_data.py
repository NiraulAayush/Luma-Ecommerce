from faker import Faker

# This file contains the login data for the tests.
# It uses the Faker library to generate random data for testing purposes.
# The data includes first name, last name, email, and password.
fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

# The register_credentials dictionary contains the generated data.
# This data will be used in the tests to register a new user on the website.
register_credentials = {
    "first_name": first_name,
    "last_name": last_name,
    "email": email,
    "password": password,
    "confirm_password": password
}

