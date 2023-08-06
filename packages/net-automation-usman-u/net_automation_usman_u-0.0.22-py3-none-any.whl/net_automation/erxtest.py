import net_automation

test_device = net_automation.Vyos(
    device_type="vyos",
    host="edge.dn42.lan",
    username="test",
    password="test",)
    # use_keys = False,
    # key_file = r"c:\Users\Usman\.ssh\id_rsa",)

test_device.init_ssh()
# print (test_device.get_version())
# ints = (test_device.get_interfaces())

# cisco = net_automation.Cisco_IOS(
#     device_type = "cisco_ios",
#     host = "2960.usman.lan",
#     username = "test",
#     password = "test",
#     secret = "test"
# )

# cisco.init_ssh()
# print (cisco.get_version())

# print (test_device.get_bgp_neighbors())

# net_automation.Vyos.deploy_yaml("vyostest.yml")

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