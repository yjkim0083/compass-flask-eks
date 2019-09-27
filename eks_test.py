from kubernetes import client, config
import json

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
nodes = v1.list_node()
#print(nodes)

# body = {
#     "metadata": {
#         "labels": {
#             "index": "01"
#         }
#     }
# }
#
# result = v1.patch_node('ip-192-168-77-134.ap-northeast-2.compute.internal', body)
# print(result)

index = 1
for i in nodes.items:
    name = i.metadata.name
    # print("=============" * 30)
    # body = {
    #     "metadata": {
    #         "labels": {
    #             "index": None
    #         }
    #     }
    # }
    # v1.patch_node(name, body)
    # index += 1
    #
    print(name)
    print(i.metadata.labels)
#
# # ret = v1.list_pod_for_all_namespaces(watch=False)
# # for i in ret.items:
# #     print(i)
# #     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))