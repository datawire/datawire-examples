#!python

import sys

import logging

logging.basicConfig(level=logging.DEBUG)

from ratings import *
from datawire_connect.resolver import DiscoveryProvider as DWCProvider
from discovery.model import Endpoint as DWCEndpoint
from discovery.client import GatewayOptions as DWCOptions

svcToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkd1R5cGUiOiJEYXRhV2lyZUNyZWRlbnRpYWwiLCJlbWFpbCI6bnVsbCwianRpIjoiZTg5ZDJiZjktYWQzZS00ZTM1LWJjNDYtYzJjODdjNjk4YjRhIiwiYXVkIjoiWkpQQTFXRjhZQyIsInNjb3BlcyI6eyJkdzpzZXJ2aWNlMCI6dHJ1ZX0sImlzcyI6ImNsb3VkLWh1Yi5kYXRhd2lyZS5pbyIsImlhdCI6MTQ1NTkyMjEyNSwib3duZXJFbWFpbCI6ImZseW5uQGRhdGF3aXJlLmlvIiwibmJmIjoxNDU1OTIyMTI1LCJzdWIiOiJyYXRpbmdzIn0.5_-uybBa2z5bjTLlTewYpTUdH572jp1DfpV4zp3fP0o'

ratings = { 'camera': 55 }

######## RATINGS MICROSERVICE
class RatingsService (object):
  """ The Ratings microservice itself. """
  def __init__(self, ratings):
    self.ratings = ratings

  def get (self, thingID):
    """ Get the rating for a given Thing. """
    rating = Rating()

    rating.thingID = thingID
    rating.rating = self.ratings[thingID]

    print("GET %s => %s" % (rating.thingID, rating.rating))

    rating.finish(None)

    return rating

######## MAINLINE

port = 8001

print("listening on port %d" % port)

url = "http://127.0.0.1:%d/" % port

# ...and fire up the ratings service.
srv = RatingsServer(RatingsService(ratings))
srv.serveHTTP(url)

endpoint = DWCEndpoint('http', '127.0.0.1', port, url)
options = DWCOptions(svcToken)
options.gatewayHost = "disco.datawire.io";

provider = DWCProvider(options, "ratings", endpoint)
provider.register(5.0)

print("...serving!")
