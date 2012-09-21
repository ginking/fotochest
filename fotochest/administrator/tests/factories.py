import factory
from fotochest.administrator.models import Settings

class SettingsFactory(factory.Factory):
    FACTORY_FOR = Settings
    
    app_name = "FotoChest"
    enable_download = True
    