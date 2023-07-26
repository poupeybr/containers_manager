import docker
from os import environ 

class ContainerHelper():
    def __init__(self):
        self.client = docker.from_env()
        dockerUsername = environ.get('DOCKER_USERNAME')
        dockerPassword = environ.get('DOCKER_PASSWORD')
        dockerRegistry = environ.get('DOCKER_REGISTRY')        
        if dockerUsername != None and dockerPassword != None and dockerRegistry != None:        
            self.client.login(username=dockerUsername, password=dockerPassword, registry=dockerRegistry)

    def does_the_container_exist(self, containername):
        containers = self.client.containers.list(
            all=True)

        containerInstance = None
        for container in containers:
            if container.name == containername:
                containerInstance = container
                break

        if containerInstance == None:
            return None
        else:
            return container

    def stop_container(self, container):
        container.stop()

    def remove_container(self, container):
        container.remove()

    def run_container(self, image, environmentVariables, volumes, name, ports, network, ip, restartPolicy):
        print("Entrou Run_Container")
        environmentList = self.map_environment(environmentVariables)
        portsList = self.map_ports(ports)
        volumesList = self.map_volumes(volumes)

        print('Iniciando execução do container')
        container = self.client.containers.create(image=image, 
                detach=True, 
                name=name, 
                ports= portsList if portsList != [] else None, 
                environment= environmentList if environmentList != [] else None,
                volumes = volumesList if volumesList != [] else None,
                restart_policy= {"Name": restartPolicy} if restartPolicy != '' else None)

        if network != None:
            self.client.networks.get(network).connect(container, ipv4_address=ip)

        result = container.start();

        print(result)

    def pull_image(self, image):
        values = image.split(':')
        print(values)
        self.client.images.pull(repository=values[0], tag=values[1])
        print("Acabou pull_images")

    def map_environment(self, environmentVariables):
        if not environmentVariables:
            return None
        
        environment = []

        for environmentVariable in environmentVariables:
            environment.append(
                f'{environmentVariable["name"]}={environmentVariable["value"]}')

        return environment

    def map_ports(self, ports):
        if not ports:
            return None
        
        portsList = dict()

        for port in ports:
            portsList[f'{port["containerPort"]}/{port["protocolPort"]}'] = port["externalPort"]

        print(portsList)
        return portsList
    
    def map_volumes(self, volumes) :
        if not volumes:
            return None
        
        volumesList = []
        
        for volume in volumes:
            volumesList.append(
                f'{volume["externalVolume"]}:{volume["containerVolume"]}'
            )
        return volumesList
