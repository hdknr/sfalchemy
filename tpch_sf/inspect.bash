#!/bin/bash
# echo $DB_URL
modelgen createmodel -s database --outfile models/models.py -p $DB_URL -a