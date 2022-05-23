The Anbox Cloud Appliance uses a self-signed certificate to provide HTTPS services. If you want to serve the appliance over HTTPS using a valid SSL/TLS certificate, follow the steps in this document to generate and install a valid SSL/TLS certificate on the Anbox Cloud Appliance.

[note type="information" status="Note"]This document assumes you have the Anbox Cloud Appliance installed. If you haven't, follow the [instructions](https://discourse.ubuntu.com/t/install-the-anbox-cloud-appliance/22681) to do so.[/note]

## Add a DNS record

Setting up DNS redirection depends on your DNS provider. Refer to the documentation of your provider to create a DNS record pointing to the IP/DNS of the AWS instance where the Anbox Cloud Appliance is running.

## Configure the location

Configure the location for the appliance using the created DNS name:

    sudo snap set anbox-cloud-appliance experimental.location=<your DNS name>

[note type="information" status="Note"]This option is experimental. It will be removed in a future release when a better replacement exists.[/note]

## Generate an SSL certificate

There are many ways to create a valid SSL certificate. One way is to use [Let's Encrypt](https://letsencrypt.org/) to generate a free SSL certificate.

First, connect and SSH into your appliance instance, and install the `certbot` snap:

    sudo snap install --classic certbot

Before generating your certificate using `certbot`, stop the Traefik service from listening on port 80 for the certificate creation:

    sudo snap stop anbox-cloud-appliance.traefik

Then run the following command to generate your certificate:

    sudo certbot certonly --standalone

This command prompts you to enter the domain name for the certificate to be generated. You will see the following message when the certificate is created successfully:

```bash
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/<your domain name>/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/<your domain name>/privkey.pem
This certificate expires on yyyy-MM-dd.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.
```

## Install the SSL certificate

Copy the generated certificate to the `/var/snap/anbox-cloud-appliance/common/traefik/tls` directory:

    sudo cp /etc/letsencrypt/live/<your domain name>/fullchain.pem /var/snap/anbox-cloud-appliance/common/traefik/tls/cert.pem
    sudo cp /etc/letsencrypt/live/<your domain name>/privkey.pem   /var/snap/anbox-cloud-appliance/common/traefik/tls/key.pem

Then start the Traefik service:

    sudo snap start anbox-cloud-appliance.traefik

With the certificate installed on the appliance, you now can access the appliance using the created domain name.

## Renew the SSL certificate

The `certbot` snap packages installed on your machine already set up a systemd timer that will automatically renew your certificates before they expire. However, in order to get the certificate renewed successfully for the appliance, you must complete the following steps:

1. Stop the Traefik service to release port 80 right before the certificate is going to be renewed. This can be done through the `pre-hook`:

   ```bash
   cat <<EOF | sudo tee /etc/letsencrypt/renewal-hooks/pre/001-stop-traefik.sh
   #!/bin/bash
   sudo snap stop anbox-cloud-appliance.traefik
   EOF
   sudo chmod +x /etc/letsencrypt/renewal-hooks/pre/001-stop-traefik.sh
   ```

2. Install the certificate right after it has been renewed and start the Traefik service through the `post-hook`:

   ```bash
   cat <<EOF | sudo tee /etc/letsencrypt/renewal-hooks/post/001-start-traefik.sh
   #!/bin/bash
   sudo cp /etc/letsencrypt/live/<your domain name>/fullchain.pem /var/snap/anbox-cloud-appliance/common/traefik/tls/cert.pem
   sudo cp /etc/letsencrypt/live/<your domain name>/privkey.pem   /var/snap/anbox-cloud-appliance/common/traefik/tls/key.pem
   sudo snap start anbox-cloud-appliance.traefik
   EOF
   sudo chmod +x /etc/letsencrypt/renewal-hooks/post/001-start-traefik.sh
   ```

In this way, the SSL certificate auto-renewal is in place.

[note type="information" status="Note"]The appliance will face a short downtime during the renewal of the SSL certificate but will come back online once the process is completed.[/note]
