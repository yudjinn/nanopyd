from enum import Enum
from math import ceil, log
from Crypto.Random import get_random_bytes


class Alphabet(Enum):
    ALPHANUMERIC = "_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    UPPERCASE = "_-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWERCASE = "_-abcdefghijklmnopqrstuvwxyz"
    NUMBERS = "0123456789"
    NO_LOOKALIKES = "_-23456789abcdefghjkmnpqrstwxyzABCDEFGHJKMNPQRSTWXYZ"


class NanoID:
    def __init__(self, alphabet: str = "alphanumeric", size: int = 21):
        if alphabet.upper() in Alphabet._member_names_:
            self.alphabet = Alphabet[alphabet.upper()].value
        elif len(alphabet) < 2:
            raise ValueError
        else:
            self.alphabet = alphabet

        self.size: int = size
        self.value: str = self.build()

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, str(self.value))

    def build(self) -> str:
        alphabet_len = len(self.alphabet)

        mask = (2 << int(log(alphabet_len - 1) / log(2))) - 1

        step = int(ceil(1.6 * mask * self.size / alphabet_len))

        nanoid = ""

        while len(nanoid) < self.size:
            random_bytes = get_random_bytes(step)
            for i in range(step):
                random_byte = random_bytes[i] & mask
                if random_byte < alphabet_len and self.alphabet[random_byte]:
                    nanoid += self.alphabet[random_byte]
                    if len(nanoid) == self.size:
                        break

        return nanoid
