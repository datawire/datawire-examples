import sys

import json
import logging
import os
import time

logging.basicConfig(level=logging.DEBUG)

from ratings import *

from datawire_connect.resolver import DiscoveryConsumer as DWCResolver
from discovery.client import GatewayOptions as DWCOptions

svcToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkd1R5cGUiOiJEYXRhV2lyZUNyZWRlbnRpYWwiLCJlbWFpbCI6bnVsbCwianRpIjoiZTg5ZDJiZjktYWQzZS00ZTM1LWJjNDYtYzJjODdjNjk4YjRhIiwiYXVkIjoiWkpQQTFXRjhZQyIsInNjb3BlcyI6eyJkdzpzZXJ2aWNlMCI6dHJ1ZX0sImlzcyI6ImNsb3VkLWh1Yi5kYXRhd2lyZS5pbyIsImlhdCI6MTQ1NTkyMjEyNSwib3duZXJFbWFpbCI6ImZseW5uQGRhdGF3aXJlLmlvIiwibmJmIjoxNDU1OTIyMTI1LCJzdWIiOiJyYXRpbmdzIn0.5_-uybBa2z5bjTLlTewYpTUdH572jp1DfpV4zp3fP0o'

print("==== Hit RETURN to start, then RETURN to make calls")

junk = sys.stdin.readline()

ratings = RatingsClient("ratings")

options = DWCOptions(svcToken)
options.gatewayHost = "disco.datawire.io"

ratings.setResolver(DWCResolver(options))

while True:
  junk = sys.stdin.readline()

  start = os.times()[4]

  wireable = ratings.get('camera')
  wireable.await(1.0)

  end = os.times()[4]
  elapsed = (end - start) * 1000

  result = None

  if wireable:
    thingID = getattr(wireable, "thingID", None)
    errString = wireable.getError()

    if errString:
      result = "BAD %s: %s" % (thingID, errString)
    else:
      rating = float(wireable.rating) / 10

      result = "OK %s: %s" % (thingID, rating)

  print("GOT %s in %dms" % (result, elapsed))
