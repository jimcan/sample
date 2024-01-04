## Products ##
# Sari-sari store
# white rabbit
# candymint
# snowbear
# sprite
# coke
# royal

## Units ##
# pcs
# 250mL

## category ##
# candy
# soft drinks

from db import get_products, delete_data

delete_data(8)

for p in get_products():
    print(p)
