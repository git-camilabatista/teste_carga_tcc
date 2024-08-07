How to run?

```sh
poetry run locust -f main.py
```

To create a graph with CPU and Memory data using psrecord lib (`poetry add psrecord` in each project)
**** testing on FASTAPI first ****

```sh
poetry run psrecord PID --interval 1 --plot my_process.png
```