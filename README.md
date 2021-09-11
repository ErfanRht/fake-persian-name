# fake-persian-name

A small Python library to generate fake Persian name.

## Install

<ul>

```
pip install fake_persian_name
```

OR:

```
pip3 install fake_persian_name
```

</ul>

## Import

<ul>

```python
from fake_persian_name import fake_name as fpn
```

</ul>

</ul>

## Use

<ul>
To generate a random Persian name:

```python
name = fpn.generate_name("random")
```

To generate a boy Persian name:

```python
name = fpn.generate_name("male")
```

To generate a girl Persian name:

```python
name = fpn.generate_name("female")
```

</ul>

## Example

<ul>

```python
from fake_persian_name import fake_name as fpn

random_name = fpn.generate_name("random")
girl_name = fpn.generate_name("female")
boy_name = fpn.generate_name("male")

print("random_name: "+random_name)
print("girl_name: "+girl_name)
print("boy_name: "+boy_name)
```

</ul>

## Issues

Please file any issues, bugs or feature request [here](https://github.com/ErfanRht/fake-persian-name/issues).

## License

This project is licensed under the [MIT License](https://github.com/ErfanRht/fake-persian-name/blob/master/LICENSE.txt)

## Author

This Python library is developed by [Erfan Rahmati](https://github.com/ErfanRht).
