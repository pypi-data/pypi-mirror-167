__version__="0.0.1"

from gnutools.fs import load_config
from gnutools.utils import RecNamespace

cfg = load_config("/opt/google_dns/config.yml")
cfg.hostnames = [RecNamespace(host) for host in cfg.hostnames]