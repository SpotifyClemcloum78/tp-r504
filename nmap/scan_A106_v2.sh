#!/bin/bash

OUTPUT_FILE="scan-result_2.csv"

echo "Lancement du scan des machines actives..."
MACHINES=$(sudo nmap -sn 172.16.0.0/24 -oG - | awk '/Up$/{print $2}')

echo "Scan des ports ouverts en cours..."

echo "IP;TCP_ports;UDP_ports" > "$OUTPUT_FILE"

TOTAL=$(echo "$MACHINES" | wc -l)
COUNT=0

for IP in $MACHINES; do
    COUNT=$((COUNT+1))
    echo "[$COUNT/$TOTAL] Analyse de $IP..."

    PORTS_TCP_OPEN=$(sudo nmap -sS -T4 -F --open --host-timeout 10s "$IP" | awk '/open/{count++} END{print count+0}')

    PORTS_UDP_OPEN=$(sudo nmap -sU -T4 -F --open --host-timeout 10s "$IP" | awk '/open/{count++} END{print count+0}')

    echo "$IP;$PORTS_TCP_OPEN;$PORTS_UDP_OPEN" >> "$OUTPUT_FILE"
done

echo "Scan terminé. Résultats enregistrés dans $OUTPUT_FILE"
