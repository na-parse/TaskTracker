#!/usr/bin/python3
# trackerService.pu
# - 
# Work Task/Activity tracking service
# Plan is to embed the emailer in this application file as well, though I might want to 
# break things out to separate library files eventually.

# Flask imports
from flask import Flask, render_template, request, redirect
# Basic Functionality
import os, json, datetime, time
# Data management and assistance
import inspect, csv, configparser

##################################################################################
# DEFINITIONS
trackerConfigFile = 'trackerConfig.json'
trackerDataFile   = 'trackerData.json'

trackerConfig = {}

trackerConfigValues = [
  'ipAddr', 'port', 
  'workerName', 'workerEmail', 
  'managerName','managerEmail', 
  'lastSentId', 'lastSentTime'
]
##############################################################################################
# FUNCTIONS Service Management
def dbgmsg(msg):
  if os.getenv('DEBUG'):
    print(f'- 


##############################################################################################
# FUNCTIONS Configuration Management
def loadConfig():
  global trackerConfig




webService = Flask(__name__)


if __name__ == '__main__':
  # CONFIG CHECK
  # Before launching the web service, we need to check if this is a first-run, or if the
  #   configuration has become corrupted.  Run a load and then run a validate.





