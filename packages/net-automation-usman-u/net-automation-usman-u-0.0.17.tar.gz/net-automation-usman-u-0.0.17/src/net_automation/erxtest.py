import net_automation

# net_automation.Vyos.deploy_yaml("erxtest.yml")

erx_zahid_lan = net_automation.EdgeOS(
    "erx.zahid.lan",
    "usman",
    "",
    True,
    r"c:\Users\Usman\.ssh\id_rsa",
)

erx_zahid_lan.init_ssh()
print (erx_zahid_lan.get_ospf_neighbours())