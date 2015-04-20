class TestACPSimulatorLibrary(object):
    """ Test Library for test acp simulator """

    def __init__(self):
        print "Init"

    def Create_Connection(self, connName, dstIp, dstPort):
        print "Create a connection named "+connName+" to "+dstIp+":"+dstPort

    def Connection_Should_Be_Created(self, connName, dstIp, dstPort):
        print "Check connection has been created."
