# nethserver-acme-dns
NethServer configuration for acme-dns (https://github.com/joohoi/acme-dns)

## Description
This package configures Nethserver 7 for acme-dns.  It contains templates for the acme-dns config file and the firewall configuration, as well as events to rebuild those files and restart the relevant services.  For further information on the purpose and usage of this package, see https://wiki.nethserver.org/doku.php?id=userguide:let_s_encrypt_acme-dns.

This will configure acme-dns to act as the authoritative nameserver for `acme.`yourdomain.

## Configuration
This package defines two configuration database keys, `acme-dns` and `acme-dns-api`.  The `acme-dns` key contains properties relevant to the DNS service itself (domain name, external IP address, log level, etc.), while the `acme-dns-api` key contains properties for the HTTP/HTTPS API (whether to use HTTPS, certificate information, whether to allow new registrations, etc.).

### acme-dns properties

|Property|Default|Description|
|-----|-----|-----|
|status|enabled|Enable or disable the acme-dns service.  Set to "disabled" to disable.|
|Domain||Root domain for the DNS server.  acme-dns will serve as the authoritative DNS server for acme.thisdomain.  Default is the primary system domain.|
|ExternalIP||IP address to serve as the A record for the acme. subdomain.  Default is the IP address of the first red interface.|
|Debug|warning|Set to "debug" to increase logfile verbosity.|

### acme-dns-api properties

|Property|Default|Description|
|-----|-----|-----|
|TCPPort|8675|Port on which the API will listen.  The API will only listen on one port, and will only do HTTP **or** HTTPS, not both (it will use HTTPS by default).|
|UseTLS|enabled|Serve the API over HTTPS rather than HTTP.  Set to "disabled" to disable (not recommended).|
|TLSType|staging|Source of TLS certificate.  Valid values are "staging" (use the Let's Encrypt staging server to avoid exceeding rate limits when testing), "letsencrypt" (obtain a production Let's Encrypt certificate), and "cert" (provide your own certificate using the FullchainPath and KeyPath keys).|
|FullchainPath|none|Path to the full certificate chain--the server cert as well as any intermediates.  This property, and KeyPath, are only used when `TLSType` is set to `cert`.|
|KeyPath|none|Path to the private key for the API|
|DisableRegistration|false|Disable new registrations to this instance of acme-dns.  If set to "true", will prevent issuance for any domains not already registered.|
|access|green|Which networks can access the API.  To access the API from the Internet, set to "green,red".|

After changing any configuration properties, rebuild the configuration file and restart the services with `signal-event nethserver-acme-dns-update`.
