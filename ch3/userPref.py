import json

def save_preferences(preferences, filepath='preferences.json'):

    """Saves user preferences dictionary to a JSON file."""

    try:

        with open(filepath, 'w') as f:

            # Save with indentation for readability

            json.dump(preferences, f, indent=4)

        print(f"Preferences successfully saved to {filepath}")

        return True

    except Exception as e:

        print(f"An error occurred while saving preferences: {e}")

        return False

# Example preferences data

current_prefs = {

    'fontSize': 12,

    'autoSave': True,

    'language': 'Python',

    'plugins': ['linter', 'debugger']

}

# Save the preferences

save_preferences(current_prefs)


