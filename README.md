# Squirrel Tracker: a Django project to track squirrels

## What is it?

**Squirrel Tracker** is a project developed with the Django framework to keep track of all the known squirrels and plans to start with Central Park. It uses [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) data and allows users to add, update, and view squirrel data.

## Who are the contributors?

### Project Group Yi & Enlu

UNIs: [yl4639, eh2926]

  - Yi Li - yl4639

  - Enlu Huang - eh2926


## Main Features

### Management Commands
  - **Import**: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 

```sh
python manage.py import_squirrel_data /path/to/file.csv
```

  - **Export**: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command.

```sh
python manage.py export_squirrel_data /path/to/file.csv
```

### Views

  - **Map View**: a view shows a map that displays the location of the squirrel sightings on an OpenStreets map.

>Located at: /map   
Method: GET   
Use the [leaflet](https://leafletjs.com/) library for plotting

  - **Sighting List View**: a view that lists all squirrel sightings with links to view each sighting.

>Located at: /sightings   
Method: GET  

  - **Update Sighting View**: a view to update a particular sighting.

>Located at: /sightings/<unique-squirrel-id>   
Method: GET & POST   

  - **Create Sighting View**: a view to create a new sighting.

>Located at: /sightings/add   
Method: GET & POST

  - **General Stats View**: a view with general stats about the sightings.

> Located at: /sightings/stats
Method: GET
