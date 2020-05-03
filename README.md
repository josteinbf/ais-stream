# Processing of AIS streams



## Generating example data for use in batch processing

To generate a sample of NMEA-formatted messages, simply use netcat:

```sh
nc 153.44.253.27 5631 | tee ais-dump.nmea
```

Simply stop netcat with a keyboard interrupt (`Ctrl-C`) when you've had enough
data. To get all AIS message types that are in the stream, it is recommended
to let the dump command run for at least 10 minutes.

There is a python script available in `data-sample/` that will parse
NMEA-encoded AIS messages and output them as json objects, one json object per
line. This script can be used to generate example data in json format. To
convert the raw, NMEA-formatted dump, simply pipe the output through the script:

```sh
# Create a virtualenv or conda env first!
pip install -r requirements.txt  # Installs dependencies
python ais_nmea_to_json.py < dump.nmea > ais-dump.jsonl
```
