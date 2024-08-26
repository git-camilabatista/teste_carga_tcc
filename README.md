# 📌 Load Test with Locust

1. Clone this project into your preferred directory:

```sh
git clone git@github.com:git-camilabatista/teste_carga_tcc.git
```

2. Navigate to the `teste_carga_tcc` directory that was created:

```sh
cd teste_carga_tcc
```

3. Run the command to install all the necessary dependencies:

> [!IMPORTANT]
> To proceed with this step, it is necessary to have [Poetry](https://python-poetry.org/) already installed.

```sh
poetry install
```

4. Navigate to the `./teste_carga_tcc/` directory:

```sh
cd teste_carga_tcc
```

5. Run the command to start Locust service:

> [!IMPORTANT]
> Before starting the Locust test, remember to start the application that will be tested.

- General tests:

This test simulates the complete flow, from user registration to purchase payment, repeating these steps for the number of users defined in the Locust settings. After performing these steps, the tests randomly list registered users, purchases, and payments to verify the load of requests that the framework can handle. For example, if you set a total of 1000 users on the Locust configuration screen, it will register these 1000 users, create a purchase for each of these users, and a payment for each purchase. Then, it will randomly access the routes for listing users, purchases, and payments to simulate the load.
  
```sh
make locust_main
```

- Test of quantity and value of purchases made:

In this test, the simulation involves registering the number of users defined in the Locust initial settings, and then the tests will create purchases and payments randomly for these created users, until the execution time defined in the initial test settings in Locust is reached. For example, if the creation of 10 users is defined, they will be created, and then purchases and payments related to these users will be made randomly until the defined execution time limit is reached. The goal of this test is to verify the number of purchases and the total value of payments that each framework can handle within a given time interval.

```sh
make locust_test_2
```

6. Access the link that is returned after running one of the commands above to view the Locust initial settings, where you can configure the test settings as desired.
   
Example of a returned link: `INFO/locust.main: Starting web interface at <LINK>`

Locust initial settings screen:
![image](https://github.com/user-attachments/assets/617eab05-c9c5-475b-94d9-0650d7bf0710)

🚩 If you are testing the [Django REST Framework](https://github.com/git-camilabatista/django_tcc) application, set the host field to: `http://127.0.0.1:8000/api`

🚩 If you are testing the [Flask Framework](https://github.com/git-camilabatista/flask_tcc) application, set the host field to:  `http://127.0.0.1:8002`

🚩 If you are testing the [FastAPI Framework](https://github.com/git-camilabatista/fastapi_tcc) application, set the host field to: `http://127.0.0.1:8001`
