# This is replaced during release process.
__version_suffix__ = '6'

APP_NAME = "zalando-kubectl"

KUBECTL_VERSION = "v1.21.5"
KUBECTL_SHA512 = {
    "linux": "0bd3f5a4141bf3aaf8045a9ec302561bb70f6b9a7d988bc617370620d0dbadef947e1c8855cda0347d1dd1534332ee17a950cac5a8fcb78f2c3e38c62058abde",
    "darwin": "4d14904d69e9f50f6c44256b4942d6623e2233e45601fb17b2b58a7f6601adacd27add292f64dbe8297f81e27052b14f83f24ef4b2ba1c84344f0169d7aa24b8",
}
STERN_VERSION = "1.19.0"
STERN_SHA256 = {
    "linux": "fcd71d777b6e998c6a4e97ba7c9c9bb34a105db1eb51637371782a0a4de3f0cd",
    "darwin": "18a42e08c5f995ffabb6100f3a57fe3c2e2b074ec14356912667eeeca950e849",
}
KUBELOGIN_VERSION = "v1.25.2"
KUBELOGIN_SHA256 = {
    "linux": "913341c90cd678ba3b7b1679d350437db9ec5779ee364858e5dea33f94c720c2",
    "darwin": "1b1b9c767e099266a842000a082c38cd5e88d5578c14b79ea284e0bf47b67a94",
}

APP_VERSION = KUBECTL_VERSION + "." + __version_suffix__
