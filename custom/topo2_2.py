from mininet.topo import Topo
class MyTopo(Topo):
"Simple topology example."
def_init_(self):
"Create custom topo."
#Initialize topology
Tpop._init_(self)
#Add hosts and switches
Host1=self.addHost('h1')
Host2=self.addHost('h2')
Host3=self.addHost('h3')
Host4=self.addHost('h4')
Switch1=self.addSwitch('s1')
Switch2=self.addSwitch('s2')
Switch3=self.addSwitch('s3')
Switch4=self.addSwitch('s4')
#Add links
self.addLink(Switch1,Switch2)
self.addLink(Switch2,Switch3)
self.addLink(Switch3,Switch4)
self.addLink(Switch1,Switch4)
self.addLink(Switch1,Host1)
self.addLink(Switch2,Host2)
self.addLink(Switch3,Host3)
self.addLink(Switch4,Host4)
topos={'mytopo':(lambda:MyTopo())}
