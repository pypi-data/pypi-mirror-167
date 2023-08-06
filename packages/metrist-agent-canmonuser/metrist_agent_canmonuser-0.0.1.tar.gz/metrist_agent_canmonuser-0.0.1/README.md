# Metrist In-Process Agent for Python

MetristAgent is the agent Python plugin. It intercepts HTTP calls and sends data to
the local Metrist Monitoring Agent

## Usage

As early in your application's lifecycle as possible, the agent should be initalized and connected:

```python
from metrist import MetristAgent

agent = MetristAgent()
agent.connect()
```

The MetristAgent constructor can take optional `host` and `port` keyword arguments
to configure the telemetry destination, otherwise it will attempt to use the
`METRIST_MONITORING_AGENT_HOST` and `METRIST_MONITORING_AGENT_PORT` environment
variables or default to `'127.0.0.1'` and `51712`.
