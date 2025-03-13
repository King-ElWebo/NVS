# Übung Subnetting

## Übung 1

Bilde aus dem Netz 192.168.0.0 /24 4 Subnetze. Netze mit Mindestzahl an nutzbaren Host aber nicht darunter wählen: Netz a mit 20, Netz b mit 15, Netz c mit 30, und das Netz d mit den Rest Anteil der Netzwerkadressen.

**Antwort**

| **Netz**  | **Netzwerkadresse** | **Subnetzmaske** | **Nutzbare Hosts** | **Erste Host-IP** | **Letzte Host-IP** | **Broadcast-Adresse** |
|-----------|---------------------|------------------|--------------------|-------------------|-------------------|--------------------|
| **A**     | 192.168.0.0/27      | 255.255.255.224  | 30                 | 192.168.0.1       | 192.168.0.30       | 192.168.0.31       |
| **B**     | 192.168.0.32/27     | 255.255.255.224  | 30                 | 192.168.0.33      | 192.168.0.62       | 192.168.0.63       |
| **C**     | 192.168.0.64/27     | 255.255.255.224  | 30                 | 192.168.0.65      | 192.168.0.94       | 192.168.0.95       |
| **D**     | 192.168.0.96/25     | 255.255.255.128  | 126                | 192.168.0.97      | 192.168.0.254      | 192.168.0.255      |


## Übung 2

Teile das Netz 193.170.20.0 /24 in 8 gleich große Netze! Erstelle eine Tabelle mit folgenden Angaben:
Netzwerkadresse,               nutzbare Hosts,                    Broadcastadresse,              Subnetzmaske.

**Antwort**

- Wir brauchen /27 dann geht sich das genau aus weil 32x8=256:
- /27 sind aber nur 30 nutzbare adressen weil die erste und letzt immer wegfällt

**Subnetztabelle**
| Netz  | Netzwerkadresse    | Nutzbare Hosts             | Broadcast-Adresse  | Subnetzmaske       |
|-------|-------------------|---------------------------|-------------------|--------------------|
| **1** | 193.170.20.0/27   | 193.170.20.1 – 193.170.20.30  | 193.170.20.31   | 255.255.255.224  |
| **2** | 193.170.20.32/27  | 193.170.20.33 – 193.170.20.62 | 193.170.20.63   | 255.255.255.224  |
| **3** | 193.170.20.64/27  | 193.170.20.65 – 193.170.20.94 | 193.170.20.95   | 255.255.255.224  |
| **4** | 193.170.20.96/27  | 193.170.20.97 – 193.170.20.126 | 193.170.20.127 | 255.255.255.224  |
| **5** | 193.170.20.128/27 | 193.170.20.129 – 193.170.20.158 | 193.170.20.159 | 255.255.255.224  |
| **6** | 193.170.20.160/27 | 193.170.20.161 – 193.170.20.190 | 193.170.20.191 | 255.255.255.224  |
| **7** | 193.170.20.192/27 | 193.170.20.193 – 193.170.20.222 | 193.170.20.223 | 255.255.255.224  |
| **8** | 193.170.20.224/27 | 193.170.20.225 – 193.170.20.254 | 193.170.20.255 | 255.255.255.224  |

**Erklärung**
- Die letzte adresse kann man nicht benutzten weil das ist die Broadcast adresse und wenn man diese benutzt und ein paket verschickt wird das an alle möglichen adressen im netz geschickt



## Übung 3

172.28.40.0 /26 Teile wie folgt auf: 2 Netze!
Erstelle eine Tabelle mit folgenden Angaben:
Netzwerkadresse,               nutzbare Hosts,                    Broadcastadresse,              Subnetzmaske.

**Antwort**

- /26 hat 64 Adressen zu verfügung
- /27 ist das größte option was man wählen kann mit jeweils 32 adressen was 2 gleich große netzwerk ergibt


**Subnetztabelle**
| Netz  | Netzwerkadresse    | Nutzbare Hosts             | Broadcast-Adresse  | Subnetzmaske       |
|-------|-------------------|---------------------------|-------------------|--------------------|
| 1 | 172.28.40.0/27   | 172.28.40.1 – 172.28.40.30  | 172.28.40.31   | 255.255.255.224  |
| 2 | 172.28.40.32/27  | 172.28.40.33 – 172.28.40.62 | 172.28.40.63   | 255.255.255.224  |


## Übung 4

Wie lautet die Subnetzmaske bei der Netzadresse: 17.0.0.0 mit 10 verwendbaren Subnetzen, sowie mit mindestens 12 Hosts je Subnetz?
Antwort in Sätzen, wie sie zu dieser Lösung kommen; und erstelle eine Tabelle:

**Antwort**

Ich würde 10 mal /28 Netzwerke benutzen weil dann habe 16 bzw 14 Netzwerkadressen zur verfüfung, dann habe ich das minimum von 12 Adressen erreicht und hätte auch theoretisch noch adressen übrig

## Übung 5

Bestimmen Sie die Subnetmaske mit folgenden Angaben:

Netzadresse: 210.52.190.0
Subnetze: Anzahl 5
Mindestanzahl von Hosts je Subnetz: 10

**Antwort**

Also man kann auch /28 nehmen weil die mindest anzahl von 10 hots mit /28 16 bzw 14 hosts zu verfüfung gestellt werden, aber chatgpt hat so gemacht deswegen nehm ich das

**Subnetztabelle**
| **Subnetz** | **Netzwerkadresse** | **Nutzbare Hosts** | **Broadcast-Adresse** | **Subnetzmaske** |
|------------|--------------------|-------------------|--------------------|-----------------|
| **1**      | 210.52.190.0/27    | 210.52.190.1 – 210.52.190.30  | 210.52.190.31  | 255.255.255.224 |
| **2**      | 210.52.190.32/27   | 210.52.190.33 – 210.52.190.62 | 210.52.190.63  | 255.255.255.224 |
| **3**      | 210.52.190.64/27   | 210.52.190.65 – 210.52.190.94 | 210.52.190.95  | 255.255.255.224 |
| **4**      | 210.52.190.96/27   | 210.52.190.97 – 210.52.190.126 | 210.52.190.127 | 255.255.255.224 |
| **5**      | 210.52.190.128/27  | 210.52.190.129 – 210.52.190.158 | 210.52.190.159 | 255.255.255.224 |



## Übung 6

Teile  ein /30 Netz auf!    Wozu werden diese /30 Netze am häufigsten verwendet?
Antwort: wenn man /30 aufteilt hat meine keine host adressen mehr zur verfüfung hat deswegen lieber lassen
bei verbindungsnetzwerken Router zu Router oder VPN verbindungen
**Antwort**

## Übung 7

Nennen Sie den jeweiligen Netz- und Hostanteil der Klassen A, B und C

**Antwort**
 
| **Klasse** | **Adressbereich** | **Subnetzmaske** | **Netzwerkanteil** | **Hostanteil** | **Max. Hosts pro Netzwerk** |
|------------|------------------|-----------------|-------------------|---------------|--------------------------|
| **A**      | 1.0.0.0 - 126.255.255.255 | 255.0.0.0  (/8)  | 8 Bits  | 24 Bits | 16.777.214 |
| **B**      | 128.0.0.0 - 191.255.255.255 | 255.255.0.0  (/16) | 16 Bits | 16 Bits | 65.534 |
| **C**      | 192.0.0.0 - 223.255.255.255 | 255.255.255.0  (/24) | 24 Bits | 8 Bits | 254 |

