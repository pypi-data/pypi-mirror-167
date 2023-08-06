"""TLS utilities."""
import ssl
from importlib import resources
from socket import socket


def setup_tls(socket: socket) -> socket:
    """Wrap a socket with a default TLS (formerly SSL) context."""
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    with (
        resources.path(__package__, "localhost.crt") as certfile,
        resources.path(__package__, "localhost.key") as keyfile,
    ):
        context.load_cert_chain(certfile, keyfile)
    return context.wrap_socket(socket, server_side=True)
