__author__ = 'sereg'

import  iptc

def allowEstablished():
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'OUTPUT')
    rule = iptc.Rule()
    match = rule.create_match('state')
    match.state = "RELATED,ESTABLISHED"
    rule.target = iptc.Target(rule, 'ACCEPT')
    chain.insert_rule(rule)

allowEstablished()