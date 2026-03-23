secret = "${MTG_SECRET_3}"
bind-to = "0.0.0.0:3128"
prefer-ip = "prefer-ipv4"

[stats.prometheus]
enabled = true
bind-to = "0.0.0.0:3129"
http-path = "/"
metric-prefix = "mtg"
