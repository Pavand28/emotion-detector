from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

# Require HTTPS in deployed environments.
# Set FORCE_HTTPS to False for local HTTP development.
Talisman(
    app,
    force_https=True,
    strict_transport_security=True,
    strict_transport_security_max_age=31536000,
    content_security_policy={
        "default-src": "'self'",
    },
)
