"""
Metrist Python In-App Agent
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Python IPA is used to time network requests made through urllib3 and submit
as telemetry through a hosted Agent.

Basic usage:
  >>> from metrist import MetristAgent
  >>> agent = MetristAgent()
  >>> agent.connect()
"""

import os
import time
import socket
import atexit
from urllib3.connectionpool import (HTTPConnectionPool, HTTPSConnectionPool)

DEFAULT_AGENT_HOST = '127.0.0.1'
DEFAULT_AGENT_PORT = '51712'

class MetristAgent:
  """Main class to manage the socket connection

  :param host: Host address of Metrist Agent to forward telemetry to. Can also be set with env `METRIST_MONITORING_AGENT_HOST`, defaults to '127.0.0.1'
  :type host: str, optional
  :param port: Port of Metrist Agent to forward telemetry to. Can also be set with env `METRIST_MONITORING_AGENT_PORT`, defaults to 51712
  :type port: int, optional
  """
  def __init__(self, **kwargs):
    """Constructor method
    """
    if 'host' in kwargs:
      self.host = kwargs['host']
    else:
      self.host = os.environ.get('METRIST_MONITORING_AGENT_HOST', DEFAULT_AGENT_HOST)

    if 'port' in kwargs:
      self.port = kwargs['port']
    else:
      self.port = int(os.environ.get('METRIST_MONITORING_AGENT_PORT', DEFAULT_AGENT_PORT))

    self.existing_urlopen = HTTPConnectionPool.urlopen
    atexit.register(lambda: self.disconnect())

  def connect(self):
    """Establish a socket connection and patch the urlopen function"""
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    HTTPConnectionPool.urlopen = self.get_patched()

  def disconnect(self):
    """Close the socket connection and restore the urlopen function"""
    self.sock.close()
    HTTPConnectionPool.urlopen = self.existing_urlopen

  def get_patched(self):
    def patched(*args, **kwargs):
      connection_pool = args[0]
      scheme = scheme_from_connection_pool(connection_pool)
      host = connection_pool.host
      address = f'{scheme}://{host}'

      method = method_from_args(*args, **kwargs)
      path = path_from_args(*args, **kwargs)

      start = time.time()
      resp = self.existing_urlopen(*args, **kwargs)
      end = time.time()

      duration = round((end - start) * 1000)

      message = f'0\t{method}\t{address}\t{path}\t{duration}'.encode()

      self.sock.sendto(message, (self.host, self.port))

      return resp
    return patched

def scheme_from_connection_pool(connection_pool):
  if isinstance(connection_pool, HTTPSConnectionPool):
    return 'https'
  return 'http'

def method_from_args(*args, **kwargs):
  if 'method' in kwargs:
    return kwargs['method']
  if len(args) >= 2:
    return args[1]
  return 'GET'

def path_from_args(*args, **kwargs):
  if 'url' in kwargs:
    return kwargs['url']
  if len(args) >= 3:
    return args[2]
  return '/'
