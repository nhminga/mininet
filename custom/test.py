if _name_ == "_main_":
    setLogLevel("info")
    OVSKernelSwitch.setup()
    intfName_1 = "eth2"
    intfName_3 = "eth3"
    info("****checking****", intfName_1, '\n')
    checkIntf(intfName_1)
    info("****checking****", intfName_3, '\n')
    checkIntf(intfName_3)

    info("****creating network****\n")
    net = Mininet(listenPort = 6633)

    mycontroller = RemoteController("muziController",   ip = "192.168.0.1")

    switch_1 = net.addSwitch('s1')
    switch_2 = net.addSwitch('s2')
    switch_3 = net.addSwitch('s3')
    switch_4 = net.addSwitch('s4')

    net.controllers = [mycontroller]


    net.addLink(switch_1, switch_2, 2, 1)# node1,   node2, port1, port2
    net.addLink(switch_2, switch_3, 2, 1)
    net.addLink(switch_1, switch_4, 3, 1)


    info("*****Adding hardware interface ",     intfName_1, "to switch:" ,switch_1.name, '\n')
    info("*****Adding hardware interface ",     intfName_3, "to switch:" ,switch_3.name, '\n')

    _intf_1 = Intf(intfName_1, node = switch_1, port =  1）
    _intf_3 = Intf(intfName_3, node = switch_3, port =  2)

    net.addLink(switch_4, switch_3, 2, 3)
    info("Node: you may need to reconfigure the     interfaces for the Mininet hosts:\n",   net.hosts, '\n')

    net.start() 
    CLI(net)   
    net.stop()  
