#!/bin/sh

# check if system is registered
subscription-manager identity > /dev/null
if [ $? -ne 0 ]; then
    echo "Please register with subscription-manager first, then re-run `katello-pull-provider-migrate.sh`."
    exit 1
fi

echo "Getting configuration from subscription-manager..."
KPPTEMPFILE=/tmp/kpp_tempfile
subscription-manager config --list > $KPPTEMPFILE
CONSUMER_CERT_DIR=$(grep 'consumercertdir' $KPPTEMPFILE | cut -d= -f2 | xargs | sed 's/[][]//g')
CERT_FILE=$CONSUMER_CERT_DIR/cert.pem
KEY_FILE=$CONSUMER_CERT_DIR/key.pem
CA_FILE=$(grep 'repo_ca_cert = ' $KPPTEMPFILE | cut -d= -f2 | xargs | cut -d ' ' -f1)
SERVER_NAME=$(grep 'hostname = ' $KPPTEMPFILE | cut -d= -f2 | xargs | cut -d ' ' -f1)

# fail if no server name, cert dir, or ca file
if [ -z "$SERVER_NAME" ] || [ -z "$CONSUMER_CERT_DIR" ] || [ -z "$CA_FILE" ]; then
    echo "Unable to determine config from `subscription-manager config --list`; exiting"
    exit 1
fi

# fail if client is not registered to a Katello
if ! grep -q 'prefix = \/rhsm' $KPPTEMPFILE; then
    echo "Client is not registered to Katello; exiting"
    exit 2
fi

rm -f $KPPTEMPFILE

# set SYSCONFDIR to /etc if it is not set
if [ -z "$SYSCONFDIR" ]; then
    SYSCONFDIR=/etc
fi

# see if /etc/yggdrasil/config.toml exists
CONFIGTOML=$SYSCONFDIR/yggdrasil/config.toml
if [ -f $CONFIGTOML ]; then
    # make a backup of CONFIGTOML
    cp $CONFIGTOML $CONFIGTOML.bak
    cat <<EOF > $CONFIGTOML
# yggdrasil global configuration settings written by katello-pull-provider-migrate

broker = ["tcp://$SERVER_NAME:1883"]
cert-file = "$CERT_FILE"
key-file = "$KEY_FILE"
ca-root = ["$CA_FILE"]
log-level = "error"
EOF

else
    echo "$SYSCONFDIR/yggdrasil/config.toml not found! Did `yum install yggdrasil` succeed?"
    exit 1
fi

# start the yggdrasild service
echo "Starting yggdrasild..."
systemctl start yggdrasild

# check status of yggdrasild and fail if it is not running
# possible failure reason: incorrect protocol (should be tcp:// or mqtt://) or port (should be 1883)
# also, cert-file and key-file must be valid
# and broker must be running on the server
yggdrasil status

if [ $(systemctl is-active yggdrasild) != "active" ]; then
    echo ""
    echo "yggdrasild failed to start! Check configuration in $CONFIGTOML and make sure the broker is running on the server."
    exit $?
fi

echo "Complete!"
