import platform

class EnvironmentInfo:
    @classmethod
    def get_os_info(cls):

        os_name = platform.system()
        os_version = platform.release()
        os_architecture = platform.architecture()[0]
        
        return {
            "os_name": os_name,
            "os_version": os_version,
            "os_architecture": os_architecture,
        }

os_info = EnvironmentInfo.get_os_info()
print(os_info)
