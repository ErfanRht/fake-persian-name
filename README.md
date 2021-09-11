# fake_persian_name

> A small Python library to generate fake Persian name.

## Instructions

1. Install:

```
pip install fake_persian_name
```

2. Import the library:

```python
from fake_persian_name import fake_name as fpn
```

3. Generate a random Persian name:

```python
name = fpn.generate_name("random")
```

4. Generate a boy Persian name:

```python
name = fpn.generate_name("male")
```

5. Generate a girl Persian name:

```python
name = fpn.generate_name("female")
```

## Example

```python
from fake_persian_name import fake_name as fpn

random_name = fpn.generate_name("random")
girl_name = fpn.generate_name("female")
boy_name = fpn.generate_name("male")

print("random_name: "+random_name)
print("girl_name: "+girl_name)
print("boy_name: "+boy_name)
```

## Issues

Please file any issues, bugs or feature request [here](https://github.com/ErfanRht/fake_persian_name/issues).

## License

This project is licensed under the [MIT License](https://github.com/ErfanRht/fake_persian_name/blob/master/LICENSE)

## Author

This Flutter package is developed by [Erfan Rahmati](https://github.com/ErfanRht).
