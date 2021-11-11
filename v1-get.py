"""
SNMPv1
++++++

Send SNMP GET request using the following options:

  * with SNMPv1, community 'nikolatee'
  * over IPv4/UDP
  * to an Agent at localhost
  * for two instances of SNMPv2-MIB::sysDescr.0 MIB object,

Functionally similar to:

| $ snmpget -v1 -c nikolatee 192.168.0.10 1.3.6.1.2.1.1.1.0

"""#
from pysnmp.hlapi import *

iterator = getCmd(
    SnmpEngine(),
    CommunityData('nikolatee', mpModel=0),
    UdpTransportTarget(('192.168.0.10', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))
)

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:
    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
