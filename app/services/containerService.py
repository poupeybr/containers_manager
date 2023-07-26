from app.helpers.containerHelper import ContainerHelper
from app.models.container import Container

class ContainerService():
    def __init__(self):
        self.containerHelper = ContainerHelper()
    

    def runcontainer(self, data):
        RUNNING = "running"
        print("Iniciando")
        
        container = self.map_to_object(data, Container)        
        
        containerInstance = self.containerHelper.does_the_container_exist(
            container.containerName)

        print(containerInstance)

        if containerInstance != None:
            print(containerInstance.status)
            if containerInstance.status == RUNNING:
                self.containerHelper.stop_container(containerInstance)

            self.containerHelper.remove_container(containerInstance)

        print("Iniciando Pull Image")
        self.containerHelper.pull_image(container.image)

        print("Iniciando Run Container")
        self.containerHelper.run_container(container.image, 
                                           container.environmentVariables,
                                           container.volumes,
                                           container.containerName, 
                                           container.ports,
                                           container.network,
                                           container.ip,
                                           container.restartPolicy)
        
    def map_to_object(self, data, obj_class):
        return obj_class(**data)
