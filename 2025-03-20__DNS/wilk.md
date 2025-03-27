- Paarbildung
- eigene und partner IP Adresse
- dig installieren

sudo apt install dnsutils -y

- Abfrage MX von whitehouse.gov
- Abfrage ip und ip6 von zdf.de

nslookup -type=AAAA zdf.de
Server:         10.255.255.254
Address:        10.255.255.254#53

Non-authoritative answer:
Name:   zdf.de
Address: 91.197.29.78

Server:         10.255.255.254
Address:        10.255.255.254#53

Non-authoritative answer:
*** Can't find zdf.de: No answer

- ping Nachbarn
- Abgabe als Screenshot oder Text (vorzugsweise)