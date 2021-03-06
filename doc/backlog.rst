######################
Luftdatenpumpe backlog
######################


******
Prio 1
******
- [o] Add PM2.5 panel again?
- [o] Add GRANT SQL statements and bundle with "--create-view" to "--setup-database"
- [o] Add "ALL" option for "Choose multiple stations" chooser


********
Prio 1.5
********
- [o] grafanimate: Monthly gif for fast progress and daily video for atmo.
- [o] grafanimate: Add "coverage" dashboard
- [o] grafanimate: Render 2015-2018 for each year
- [o] Stats: Until 2016, it's around 1M files, 600MB data in InfluxDB and 17M P1 readings
- [o] Is it actually ok to read each sensor equally?
- [o] Downsample data on CSV import to reduce data size?
- [o] Read Parquet files from http://archive.luftdaten.info/parquet/
- [o] Vanity URLs
    - https://deutschland.maps.luftdaten.info
    - https://china.maps.luftdaten.info
    - https://europe.maps.luftdaten.info
    - https://france.maps.luftdaten.info/


******
Prio 2
******
- [o] Use https://grafana.com/plugins/ryantxu-ajax-panel to show other content
- [o] What to do with high P1/P2 values > 1.000 and more?
- [o] CSV import: Add more sensor types
- [o] Link from sticky overlay to station trend dashboard
- [o] Refactor for handling multiple data sources and targets
- [o] Run some metric about total count of measuremnts per feed action
- [o] Use more export formats from tablib
- [o] Output data in tabular, markdown or rst formats
- [o] Publish to MQTT with separate topics
- [o] Store "boundingbox" attribute to RDBMS database
- [o] Dry-run for RDBMS storage
- Command line filters
    - [o] by sensor type
    - [o] by time range. e.g. for CSV file import.
- Grafana Worldmap Panel
    - [o] Handle multiple languages with Nominatim. Use English as default.
    - [o] Get English (or configurable) country labels from Nominatim
    - [o] JSON endpoint: Add formatter ``jq '[ .[] | {key: .station_id | tostring, name: .name} ]'``
    - [o] JSON endpoint: Map by geohash only
    - [o] Link to Nominatim place_id, see https://nominatim.hiveeyes.org/details.php?place_id=8110875
- [o] Migration documentation from https://getkotori.org/docs/applications/luftdaten.info/
- [o] Mention other projects

    - https://luftdata.se/

- [o] How to improve Grafana Worldmap Panel JSON document becoming stale?
      /public/json/ldi-stations.json?_cache=4

- [o] Check out wizzy for Grafana provisioning?
  https://github.com/utkarshcmu/wizzy

- [o] Docs? https://github.com/grafana/worldmap-panel/issues/176


******
Prio 3
******
- [o] OSM: Why are some roads or towns empty?
      weatherbase=# select * from ldi_osmdata where road is null limit 7;
- [o] Add remark after "licence": "Data \u00a9 OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright" like
      "remark": "The address information has been modified by luftdatenpumpe 0.4.0"
- [o] OSM: English labels for e.g. Hercegovine, BA
- [o] Database view
      https://www.postgresql.org/docs/9.2/sql-createview.html
      on top of
      https://community.hiveeyes.org/t/erneuerung-der-luftdatenpumpe/1199/25
- [o] Integrate https://github.com/openaq/openaq-fetch somehow


******
Prio 4
******
- [o] Write metadata directly to PostGIS
  https://dataset.readthedocs.io/en/latest/
- [o] Add support for JSON and GIS data to "dataset" module
- [o] OSM: Italia only has 3-letter state names like CAL, CAM, LOM, etc.
- [o] Add PostgREST
- [o] Grafana: Link to https://www.madavi.de/sensor/graph.php and/or
      http://deutschland.maps.luftdaten.info/#13/50.9350/13.3913 and/or
      https://maps.luftdaten.info/grafana/d-solo/000000004/single-sensor-view?orgId=1&panelId=1&var-node=18267
      somehow?
- [o] After importing historical data, make a video from the expanding map
- [o] Update

    - https://github.com/opendata-stuttgart/sensors-software/issues/33
    - https://twitter.com/SchindlerTimo/status/1064634624192774150

- [o] Provide jq examples


- [o] Grafana::

    Appendix
    ========

    Add text widget containing total number of stations in database.

    Variable ``station_count```::

        SHOW TAG VALUES CARDINALITY WITH KEY = station_id;


****
Done
****
- [x] Download cache for data feed (5 minutes)
- [x] Write metadata directly to Postgres
- [x] Redesign commandline interface
- [x] Create CHANGES.rst, update documentation and repository (tags)
- [x] Add tooling for packaging
- [x] Publish to PyPI
- [x] Write measurement data directly to InfluxDB
- [x] Store stations / data **while** processing
- [x] Make a sensor type chooser in Grafana. How would that actually select
      multiple(!) stations by id through Grafana?
- [x] Store Geohash into InfluxDB database again. Check for sensor_id.
- [x] Probe Redis when starting
- [x] Add Grafana assets
- [x] Import historical data from http://archive.luftdaten.info/
- [x] Check User-Agent settings
- [x] Overhaul station metadata process:
      1. Collect station information from API or CSV into PostgreSQL
      2. Export station information from PostgreSQL as JSON, optionally in format suitable for Grafana Worldmap Panel
- [x] Improve README
    - [x] Add link to Demo #5
    - [x] Mention InfluxDB storage and historical data
    - [x] Add some screenshots
- [x] Add more sensors:
    - archive.luftdaten.info/2017-10-08/2017-10-08_pms3003_sensor_366.csv
    - archive.luftdaten.info/2017-10-08/2017-10-08_pms7003_sensor_5920.csv
    - archive.luftdaten.info/2017-11-25/2017-11-25_hpm_sensor_7096.csv
    - archive.luftdaten.info/2017-11-26/2017-11-26_bmp280_sensor_2184.csv
    - archive.luftdaten.info/2017-11-26/2017-11-26_htu21d_sensor_2875.csv
- [x] Speed up CSV data import using UDP?
- [x] Add PostgreSQL view "ldi_view" with ready-computed name+station_id things and more
- [x] Improve RDBMS database schema
    - [x] Rename "weatherbase" to "weatherbase"
    - [x] Rename id => station_id
    - [x] Rename osm => osm_*
    - [x] Rename ldi_view => ldi_network
- [x] Fix Grafana vt+kn exports
- [x] Overhaul Grafana dashboards
- [x] Display number of sensors per family
- [x] Remove --help from README
- [x] Improve README re. setup
- [x] Entrypoints for rendering Grafana JSONs
- [x] WARNING: Skip import of /datalarge/var/spool/archive.luftdaten.info/2019-01-02/2019-01-02_ds18b20_sensor_8020.csv. Unknown sensor type
- [x] Add station_id to "choose multiple stations" chooser
- [x] Fix fix fix::

    2019-01-21 02:54:44,787 [luftdatenpumpe.core           ] WARNING: Could not make reading from {'sensordatavalues': [{'value': '81.40', 'value_type': 'humidity', 'id': 5790214143}, {'value': '0.20', 'value_type': 'temperature', 'id': 5790214142}], 'sensor': {'sensor_type': {'name': 'DHT22', 'manufacturer': 'various', 'id': 9}, 'pin': '7', 'id': 19755}, 'timestamp': '2019-01-21 01:50:56', 'id': 2724801826, 'location': {'longitude': '', 'latitude': '47.8120', 'altitude': '58.0', 'country': 'DE'}, 'sampling_rate': None}.
    Traceback (most recent call last):
      File "/opt/luftdatenpumpe/luftdatenpumpe/core.py", line 230, in request_live_data
        reading = self.make_reading(item)
      File "/opt/luftdatenpumpe/luftdatenpumpe/core.py", line 290, in make_reading
        self.enrich_station(reading.station)
      File "/opt/luftdatenpumpe/luftdatenpumpe/core.py", line 308, in enrich_station
        station.position.geohash = geohash_encode(station.position.latitude, station.position.longitude)
      File "/opt/luftdatenpumpe/luftdatenpumpe/geo.py", line 351, in geohash_encode
        geohash = geohash2.encode(float(latitude), float(longitude))
    TypeError: float() argument must be a string or a number, not 'NoneType'

