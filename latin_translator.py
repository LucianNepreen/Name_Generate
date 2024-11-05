import json
import glob

def load_translations(file_path):
	translations = {}
	for file_path in file_paths:
	    with open(file_path,'r', encoding='utf-8') as file:
		    translations.update(json.load(file))
	return translations


def translate_to_latin(word, translation_dict):
	"""Translate an English word to Latin using dictionary"""
	return translation_dict.get(word.lower(), "Translation not found.")

def main():
	print("Welcome to the Latin Translator!")


	# Load translations from the JSON file
	json_files = glob.glob('translations*.json')
	translation_dict = load_translations('translations.json')


	while True:
		word = input("Enter an Englsh word to translate (or 'exit' to quit): ")
		if word.lower() == 'exit' :
			print("Goodbye!")
			break
		translation = translate_to_latin(word, translation_dict)
		print(f"Latin translation: {translation}")


	if __name__ == "__main__":
		main()