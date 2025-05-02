from settings_management  import ApplicationConfig
from dotenv import dotenv_values

env_values = dotenv_values(".env")

print(env_values.values())
try:
    config = ApplicationConfig(**env_values)
    print("Database Configuration:")
    print("Database Host: ", config.database_host)
    print("Database User: ", config.database_user)
    print("Database Password", config.database_password)
    print("API Key: ", config.api_key)

except Exception as e:
    print("Validation Error: ", e)

