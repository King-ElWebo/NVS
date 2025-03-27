Wurde mit ChatGPT in ein schönes markdown Format gebracht

# 🌐 Netzwerktechnik - Aufgabenprotokoll

**Paarbildung:** Sebastian Kurta  

---

## 🖥️ Eigene und Partner IP-Adresse

| Gerät           | IPv4-Adresse      | MAC-Adresse          |
|-----------------|-------------------|----------------------|
| **Eigener PC**  | `192.168.33.146`  | `14-AC-60-52-FE-2D`  |
| **Partner PC**  | `192.168.33.145`  | `14-CE-51-17-AF-86`  |

---

## ⚙️ Installation von `dig`

Installation der DNS-Tools mit folgendem Befehl:

```bash
sudo apt install dnsutils -y
```
Abfrage MX von whitehouse.gov

```bash
; <<>> DiG 9.18.30-0ubuntu0.24.04.2-Ubuntu <<>> mx whitehouse.gov
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 3630
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;whitehouse.gov.                        IN      MX

;; AUTHORITY SECTION:
whitehouse.gov.         1800    IN      SOA     ernest.ns.cloudflare.com. dns.cloudflare.com. 2368069009 10000 2400 604800 1800

;; Query time: 30 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Thu Mar 27 17:30:39 CET 2025
;; MSG SIZE  rcvd: 107
```
Abfrage ip und ip6 von zdf.de
```bash
nslookup -type=AAAA zdf.de
Server:         10.255.255.254
Address:        10.255.255.254#53

Non-authoritative answer:
Name:   zdf.de
Address: 91.197.29.78

Server:         10.255.255.254
Address:        10.255.255.254#53

```
ping Nachbarn
```bash
Ping wird ausgeführt für 192.168.33.145 mit 32 Bytes Daten:
Antwort von 192.168.33.145: Bytes=32 Zeit=6ms TTL=128
Antwort von 192.168.33.145: Bytes=32 Zeit=6ms TTL=128
Antwort von 192.168.33.145: Bytes=32 Zeit=4ms TTL=128
Antwort von 192.168.33.145: Bytes=32 Zeit=5ms TTL=128

Ping-Statistik für 192.168.33.145:
    Pakete: Gesendet = 4, Empfangen = 4, Verloren = 0
    (0% Verlust),
Ca. Zeitangaben in Millisek.:
    Minimum = 4ms, Maximum = 6ms, Mittelwert = 5ms
