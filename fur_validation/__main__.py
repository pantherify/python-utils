from .src.fur_validation import Fur

fur = Fur()
keyring = fur.generate_keyring()

print(keyring)
