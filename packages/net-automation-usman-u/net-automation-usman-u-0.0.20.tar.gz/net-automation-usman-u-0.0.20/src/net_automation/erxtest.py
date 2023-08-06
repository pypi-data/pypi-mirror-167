import net_automation

net_automation.Vyos.deploy_yaml("vyostest.yml")

# erx_lan = net_automation.EdgeOS(
#     "ubiquiti_edgerouter",
#     "erx.zahid.lan",
#     "usman",
#     "",
#     True,
#     r"c:\Users\Usman\.ssh\id_rsa",
# )

# erx_lan.init_ssh()
# print (erx_lan.get_ospf_neighbours())
# # print (erx_lan.get_ospf_route())

# print (erx_lan.get_ospf_route("10.100.100.4"))
# print (erx_lan.get_ospf_route("10.100.100.1"))


# edge = net_automation.Vyos(
#     "vyos",
#     "edge.dn42.lan",
#     "test",
#     "test",
#     False,
#     "",
# )
# print (edge.get_route_table(modidier="ospf", test="t"))
# # edge.init_ssh()
# # print (edge.get_ospf_neighbours())
# # print (edge.get_route("10.0.10.1"))