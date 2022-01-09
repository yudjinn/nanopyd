## NanoPyD

### Python NanoID with class typing.

Builds a Nano ID per spect defined by [this repo](https://github.com/ai/nanoid).

## Installation and Usage:

    `pip install nanopyd`

    `from nanopyd import NanoID`

    `id : NanoID = NanoID()`

### Parameters:

1. alphabet :
   - **"alphanumeric"**= "\_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
   - "uppercase" = "\_-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   - "lowercase" = "\_-abcdefghijklmnopqrstuvwxyz"
   - "numbers" = "0123456789"
   - "no_lookalikes" = "\*-23456789abcdefghjkmnpqrstwxyzABCDEFGHJKMNPQRSTWXYZ"
2. size :
   - length of output id, default **21**
