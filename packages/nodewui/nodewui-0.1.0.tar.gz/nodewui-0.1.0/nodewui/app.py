#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import json
import requests
import configparser

import cherrypy

__version__ = 0.1

# get configuration file location from first command line argument
config_file = sys.argv[1:]

# Configpraser does not recognize files without sectsions, so we add one
with open(config_file[0], 'r') as f:
    config_string = '[main]\n' + f.read()
    
config = configparser.ConfigParser()
config.read_string(config_string)



# Get rpc url from enviroment variable or use default
rpc_url = os.getenv('rpc_url', "http://127.0.0.1")
# Get network type from enviroment variable or use default
network = os.getenv('network', "")
web_port = os.getenv('web_port', 8080)
listening_ip = os.getenv('listening_ip', "127.0.0.1")

# Get rpc user and password from configuration file
rpc_password = config["main"]["rpcpassword"]
rpc_user = config["main"]["rpcuser"]

# Read test4 section of the configuration file if exist and network is testnet4
if config.has_section("test4") and network == "bch_testnet4":
    rpc_port = config["test4"]["rpcport"]
else:
    rpc_port = config["main"]["rpcport"]

# Create full RPC URL from url + port
url = rpc_url + ":" + rpc_port + "/"


cherrypy.log(
            f"url: {url} # network: {network}"
            )


# Cherrypy: Location of media dir
MEDIA_DIR = os.path.join(os.path.abspath("."), u"media")


def call_rpc(payload):
    """
    Function to call RPC with a provided method
    """ 
    cherrypy.log(f"payload: {payload}")
    # Headers to be provided in requests function query
    headers = {'content-type': 'application/json', 'cache-control': 'no-cache'}
    # log headers using cherrypy log, useful for debuging
    cherrypy.log(f'headers: {headers}')
    # Try to call RPC and show exceptions if there is an issue
    try:
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=(rpc_user, rpc_password)
            )
        # The function will return the response of the request in json format
        return json.loads(response.text)
    # If there is an issue related to Request it will report request issue
    except requests.exceptions.RequestException as e:
        cherrypy.log(f"Request issue: {e}")
    # If there is an issue it will report it
    except Exception as e:
        cherrypy.log(f"Error: {e}")


class BlockchainRPC(object):
    @cherrypy.expose
    def index(self):
        """Index page of the app"""
        return open(os.path.join('media/index.html'))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get(self, **params):
        test = json.dumps(params, indent=4, sort_keys=True)
        cherrypy.log(f"json dump of params: {test}")
        # Construct payload from provided method in json format 
        if not params.get("params"):
            _params = []
            cherrypy.log("empty parameters list")
        elif type(params.get("params")) != list:
            _params = [params.get("params")]
            cherrypy.log("type is not list")
        else:
            _params = params.get("params")
            cherrypy.log("anything else")
        payload = json.dumps({"method": params["method"], "params": _params}) # have the method in 
        cherrypy.log(payload)
        return call_rpc(payload)

    # ~ @cherrypy.expose
    # ~ @cherrypy.tools.json_out()
    # ~ def listtransactions(self):
        # ~ return call_rpc('listtransactions')

    # ~ @cherrypy.expose
    # ~ @cherrypy.tools.json_out()
    # ~ def getbalance(self):
        # ~ return call_rpc('getbalance')

    # ~ @cherrypy.expose
    # ~ @cherrypy.tools.json_out()
    # ~ def getelectruminfo(self):
        # ~ return call_rpc('getelectruminfo')

    # ~ @cherrypy.expose
    # ~ @cherrypy.tools.json_out()
    # ~ def getmininginfo(self):
        # ~ return call_rpc('getmininginfo')
        
    # ~ @cherrypy.expose
    # ~ @cherrypy.tools.json_out()
    # ~ def getpeerinfo(self):
        # ~ return call_rpc('getpeerinfo')
        
    # ~ @cherrypy.expose
    # ~ @cherrypy.tools.json_out()
    # ~ def getnewaddress(self):
        # ~ return call_rpc('getnewaddress')        


config = {'/media':
   {'tools.staticdir.on': True,
   'tools.staticdir.dir': MEDIA_DIR,}
}

# Option to set the port of the server
cherrypy.config.update({'server.socket_port': web_port})

# Set server to listen to all
cherrypy.server.socket_host = listening_ip

# Run the application 
cherrypy.quickstart(BlockchainRPC(), '/', config=config)
