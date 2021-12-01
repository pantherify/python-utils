from .src.fur_validation.core import Fur

fur = Fur()
keyring = fur.generate_keyring()

print(keyring)
