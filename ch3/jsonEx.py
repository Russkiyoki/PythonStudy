import json

# has an optional parameter, because config.json is the default value
# can be different 
def load_config(filepath='config.json'):
	# loads config settings from a json file

	try:
		with open(filepath, 'r') as f:
			config = json.load(f)
			return config

	except FileNotFoundError:
		print("Couldnt find the file!")
		return None

	except json.JSONDecodeError:
		print(f"Error decoding from: {filepath}")
		return None

	except Exception as e:
		print(f"An error occured while loading the config: {e}")
		return None

# Loading the config

app_config = load_config()

if app_config:
	print("\nConfiguration loaded:")
	print(f"Database URL: {app_config.get('database_url')}")
	print(f"API Key: {app_config.get('api_key')}")

	if 'feature_flags' in app_config:
		print(f"New Dashboard Enabled: {app_config['feature_flags'].get('new_dashboard')}")
