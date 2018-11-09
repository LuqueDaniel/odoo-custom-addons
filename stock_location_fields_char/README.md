# Stock Location Fields Char
This addon replaces the `int` fields of the `stock.location` model with new ones of type `char`.

## Features
- Hides the fields `posx`,` posy` and `posz`. These fields indicate the location in the locations (aisle, shelf, height).
- Add the following fields: `x_posx`,` x_posy` and `x_posz`. These fields are alphanumeric, with a maximum size of 10 characters.
- Modify the views to use the new fields instead of the ones by default.

## Depends of
- `stock`
