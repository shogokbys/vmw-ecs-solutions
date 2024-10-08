## Instruction

Once the node-red is procured, the web console is accessible through http://<worker node ip>:31880

1. Access web console at http://<worker node ip>:31880
2. Settings > Palette > Install
3. Search required nodes and install
- node-red-contrib-modbus
- node-red-contrib-opcua
- node-red-contrib-postgresql
4. Download `sample_flow.json` from this directory
5. Import `sample_flow.json`

## What this sample flow is doing?

- polls opc-ua server(i.e. simulated temperature sensor and pressure sensor) every 1 minute and store the value in postgresql
- Delete records in postgresql server older than 6 hours to conserve the storage usage

