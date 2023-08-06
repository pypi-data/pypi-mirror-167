import requests

DEFAULT_CP_PORT: str = "443"
# LEGACY_CP_PORT is defined here to ensure backward compatibility with old Control Planes
# that use the legacy port 8000. This should be removed once we no longer need to support
# Control Planes that use port 8000.
LEGACY_CP_PORT: str = "8000"
CP_ENDPOINT: str


def define_cp_endpoint(cp_address: str):
    global CP_ENDPOINT
    # Port 8000 must be tested first since the Control Planes
    # that use port 8000 expose ping on both ports (8000 for
    # Kong and 443 for Jeeves).
    possible_ports = [LEGACY_CP_PORT, DEFAULT_CP_PORT]
    for port in possible_ports:
        try:
            # If the Control Plane uses the legacy port 8000, the port must be
            # specified together with the Control Plane address. Otherwise, if
            # the Control Plane uses the default port 443, the port can be omitted.
            cp_endpoint = (
                f"{cp_address}:{port}" if port == LEGACY_CP_PORT else cp_address
            )
            url = f"https://{cp_endpoint}/ping"
            response = requests.get(url=url, timeout=3)
            response.raise_for_status()
            CP_ENDPOINT = cp_endpoint
            return
        except (
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ConnectionError,
        ):
            continue
    raise Exception(
        f"Couldn't figure out the port for the following Control Plane address: {cp_address}"
    )
