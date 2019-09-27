from kubernetes import client, config

class EKSManager:
    def __init__(self, cluster_name):
        self.cluster_name = cluster_name

    def updateKubeConfig(self):
        '''
        EKS_CLUSTER_NAME을 입력받아서 kubeconfig를 update 한다
        :return:
        '''
        pass

        pass

    def getClusterName(self):
        return self.cluster_name

    def getEKSInfo(self):
        # Configs can be set in Configuration class directly or using helper utility
        config.load_kube_config()
        v1 = client.CoreV1Api()
        ret = v1.list_pod_for_all_namespaces(watch=False)

        info = []
        for i in ret.items:
            _info = {}
            _info["ip"] = i.status.pod_ip
            _info["namespace"] = i.status.namespace
            _info["name"] = i.status.name
            info.append(_info)
            #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

        return info
