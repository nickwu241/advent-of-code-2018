#!/bin/sh
set -euo pipefail

if [ $# -ne 1 ]; then
    echo "usage: $0 <DAY_NUMBER>"
fi

mkdir "day$1"
touch "day$1/input"
cat <<EOF > "day$1/day$1.py"
#!/usr/bin/env python
with open('input') as f:
    pass

# Puzzle 1

# Puzzle 2
EOF
chmod +x "day$1/day$1.py"
