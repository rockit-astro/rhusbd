## RH-USB sensor daemon

`rhusbd` wraps an Omega Engineering RH-USB probe and makes the latest measurement available for other services via Pyro.

`rhusb` is a commandline utility that reports the latest data from a probe.

### Configuration

Configuration is read from json files that are installed by default to `/etc/rhusbd`.
A configuration file is specified when launching the server, and the `rhusb` frontend will search this location when launched.

```python
{
  "daemon": "warwick_rhusb", # Run the server as this daemon. Daemon types are registered in `rockit.common.daemons`.
  "log_name": "rhusbd@warwick", # The name to use when writing messages to the observatory log.
  "serial_port": "/dev/rhusb", # Serial FIFO for communicating with the vaisala
  "serial_baud": 9600, # Serial baud rate
  "serial_timeout": 5, # Serial comms timeout
  "loop_delay": 5 # Delay between sensor queries
}
```

### Initial Installation

The automated packaging scripts will push 4 RPM packages to the observatory package repository:

| Package                   | Description                                                                   |
|---------------------------|-------------------------------------------------------------------------------|
| rockit-rhusb-server       | Contains the `rhusbd` server and systemd service file.                        |
| rockit-rhusb-client       | Contains the `rhusb` commandline utility for controlling the rhusb server.    |
| rockit-rhusb-data-warwick | Contains the json configuration and udev rules for the Windmill Hill station. |
| python3-rockit-rhusb      | Contains the python module with shared code.                                  |

Alternatively, perform a local installation using `sudo make install`.

After installing packages, the systemd service should be enabled:

```
sudo systemctl enable --now rhusbd@<config>
```

where `config` is the name of the json file for the appropriate unit.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `rockit.common.daemons` for the daemon specified in the config.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl restart rhusbd@<config>
```

### Testing Locally

The server and client can be run directly from a git clone:
```
./rhusbd ./warwick.json
RHUSBD_CONFIG_PATH=./warwick.json ./rhusb status
```
