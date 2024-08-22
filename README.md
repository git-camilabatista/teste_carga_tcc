How to run?

```sh
poetry run locust -f main.py --processes 4

poetry run locust -f test_2.py --processes 4
```

or using Makefile

```sh
make locust_main

make locust_test_2
```