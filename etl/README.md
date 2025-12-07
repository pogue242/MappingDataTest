## ETL : Create Database

### Purpose
a Python script to:
- Extract data from NYC Open data APIs & ultilizize Google Earth engine's images on NYC's surface temperature
- Transform that data to fit the business requirments
- export an GeoJson file

### Technologies
- Python
- Pandas
- GeoPandas
- Requests

### How to run : With Docker
- Make sure you have Docker desktop downloaded, if you don't go [here](https://www.docker.com/products/docker-desktop/)
- create an .env file with the API_TOKEN variable defined with the API key
- run this command in your terminal:
    ```console

        docker build --secret id=API_TOKEN,env=API_TOKEN -t etl:latest  ./etl 

    ```
- Then run this command to execute the program:
    ```console

        docker run etl:latest

    ```
