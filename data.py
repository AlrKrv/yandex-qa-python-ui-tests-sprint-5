import helpers
user = [
    'Alexander',
    'al_kr_16@ya.ru',
    '123456'
]

user_name = helpers.UserDataGenerator.generate_name()
mail = helpers.UserDataGenerator.generate_email()
password = helpers.PasswordGenerator.generate_password()