This example implementation provides a starting point for a monitoring stack that can be used to monitor the status of your Anbox Cloud cluster using [Nagios](https://www.nagios.org/), a tool that is widely used for monitoring networks, servers and applications. Using the Nagios Remote Plugin Executor (NRPE) on each node, it can monitor your cluster with machine-level detail.

[note type="information" status="Important"]This reference implementation is provided for demonstration purposes only. It does not cover all aspects that you should consider for a production-level solution (for example, high availability).[/note]

In this setup, Anbox Cloud integrates with Nagios and allows you to monitor the status of its services to be alerted when something goes wrong.

Nagios monitors the following services:

- AMS
- LXD
- AMS Node Controller
- Anbox Stream Gateway
- Anbox Stream Agent
- Coturn

## Deploy the solution

The monitoring stack is provided as an [overlay file](https://discourse.ubuntu.com/t/installation-customizing/17747#overlay-files) that you use when deploying Anbox Cloud.

The overlay installs Nagios on one machine and the Nagios Remote Plugin Executor (NRPE) on all machines. In addition, it creates the required relations.

Complete the following steps to deploy Anbox Cloud with the reference monitoring stack:

1. Create a `nagios.yaml` file with the following content, depending on which [Juju bundle](https://discourse.ubuntu.com/t/about-anbox-cloud/17802#juju-bundles) you want to deploy:

   [Details="For the `anbox-cloud-core` bundle"]
   ```yaml
   applications:
     nagios:
       charm: 'cs:nagios'
       expose: true
       num_units: 1
       to:
         - '2'
     nrpe:
      charm: 'cs:nrpe'

   relations:
     - ['ams', 'nrpe:nrpe-external-master']
     - ['lxd', 'nrpe:nrpe-external-master']
     - ['ams-node-controller', 'nrpe:nrpe-external-master']
     - ['nrpe', 'nagios']

   machines:
     '0':
       series: bionic
       constraints: "cpu-cores=4 mem=4G root-disk=40G"
     '1':
       series: bionic
       constraints: "cpu-cores=8 mem=16G root-disk=50G"
     '2':
       series: bionic
       constraints: "cpu-cores=2 mem=8G root-disk=10G"
   ```
   [/Details]

   [Details="For the `anbox-cloud` bundle"]
   ```yaml
   applications:
     nagios:
       charm: 'cs:nagios'
       expose: true
       num_units: 1
       to:
         - '2'
     nrpe:
      charm: 'cs:nrpe'

   relations:
     - ['ams', 'nrpe:nrpe-external-master']
     - ['lxd', 'nrpe:nrpe-external-master']
     - ['ams-node-controller', 'nrpe:nrpe-external-master']
     - ['nrpe', 'nagios']
     - ['anbox-stream-gateway', 'nrpe:nrpe-external-master']
     - ['anbox-stream-agent', 'nrpe:nrpe-external-master']
     - ['coturn', 'nrpe:nrpe-external-master']

   machines:
     '0':
       series: bionic
       constraints: "cpu-cores=4 mem=4G root-disk=40G"
     '1':
       series: bionic
       constraints: "cpu-cores=8 mem=16G root-disk=50G"
     '2':
       series: bionic
       constraints: "cpu-cores=2 mem=8G root-disk=10G"
   ```
   [/Details]
1. Deploy Anbox Cloud with the overlay file.

   - For the `anbox-cloud-core` bundle:

         juju deploy cs:~anbox-charmers/anbox-cloud-core-89 --overlay nagios.yaml

   - For the `anbox-cloud` bundle:

         juju deploy cs:~anbox-charmers/anbox-cloud-103 --overlay nagios.yaml

   [note type="information" status="Note"]You can use the same command if you already deployed Anbox Cloud. In this case, Juju checks the existing deployment and only deploys new components.[/note]
1. Wait until all added units are in `active` state.

### Use an existing Nagios service

If you already have an existing Nagios installation, adapt the overlay file to only install the NRPE charm on all machines.

After deployment, configure the NRPE charm to work with your existing Nagios installation:

    juju config nrpe export_nagios_definitions=true
    juju config nrpe nagios_master=<ip-address-of-nagios>

See the [External Nagios](https://jaas.ai/nrpe) section of the NRPE charm README for more information.

## Access Nagios

To access the Nagios web interface, go to `http://<IP_address>/` in your browser.

Replace `<IP_address>` with the IP address of the machine on which you deployed Nagios. If you don't know the address, run the following command:

    juju status --format yaml nagios/0 | grep public-address

[note type="information" status="Note"]If you have deployed more than one Nagios unit, you might need to replace the `0` in `nagios/0` with the suitable unit ID. Check `juju status` if you are in doubt.[/note]

You must enter your user name and password to log in. The user name is `nagiosadmin`. You can determine the password by running the following command (note that you might need to replace the `0` as mentioned above):

    juju ssh nagios/0 sudo cat /var/lib/juju/nagios.passwd
