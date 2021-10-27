
# Coin Mena

This is Django and Django Rest Framework Project for getting data from alphavantage.co website api for every hour and store it in postgresql database.

## Acknowledgements

 - [Alphavantage](https://www.alphavantage.co/)
 
  
## API Reference

#### Get the exchange rate

```http
  GET /api/quotes
```

#### Trigger the data from alphavantage

```http
  POST /api/quotes/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `from_currency_code`      | `string` | **Required**. |
`to_currency_code`      | `string` | **Required**.  |

  
## Deployment

To deploy this project run

```bash
  docker-compose up --build
```

  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

```bash
API_KEY=RK1H2OT037M548B4
DB_HOST=pgdb
DB_NAME=coinmena
DB_USER=postgres
DB_PASS=12345
POSTGRES_DB=coinmena
POSTGRES_USER=postgres
POSTGRES_PASSWORD=12345
TIME_INTERVAL=1
```

  
## Screenshots

![](https://github.com/chezhian-softsuave/coinmena/blob/master/screenshots/apiscreen1.png)
![](https://github.com/chezhian-softsuave/coinmena/blob/master/screenshots/apiscreen2.png)

## Database Structure - ER Diagram
![](https://github.com/chezhian-softsuave/coinmena/blob/master/screenshots/dbstructure.png)

## Run Locally

Clone the project

```bash
  git clone https://github.com/chezhian-softsuave/coinmena.git
```

Go to the project directory

```bash
  cd coinmena
```

Install dependencies

```bash
   docker-compose up --build
```

open the browser and type

```bash
   http://localhost:8000
```

## To run the testcases

```bash
   python manage.py test
```


  
