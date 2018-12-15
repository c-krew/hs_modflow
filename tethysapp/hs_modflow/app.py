from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import PersistentStoreDatabaseSetting


class HsModflow(TethysAppBase):
    """
    Tethys app class for Hydroshare Modflow Visualization.
    """

    name = 'Hydroshare Modflow Visualization'
    index = 'hs_modflow:home'
    icon = 'hs_modflow/images/icon.gif'
    package = 'hs_modflow'
    root_url = 'hs-modflow'
    color = '#2c3e50'
    description = 'runs modflow models that are stored in hydroshare'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='hs-modflow',
                controller='hs_modflow.controllers.home'
            ),
            UrlMap(
                name='load-resource',
                url='hs-modflow/load-resource',
                controller='hs_modflow.model.load_resource'
            ),
            UrlMap(
                name='search',
                url='hs-modflow/search',
                controller='hs_modflow.ajax_controllers.search'
            ),
            UrlMap(
                name='load-text-file',
                url='hs-modflow/load-text-file',
                controller='hs_modflow.ajax_controllers.load_text_file'
            ),
            UrlMap(
                name='save-text-file',
                url='hs-modflow/save-text-file',
                controller='hs_modflow.ajax_controllers.save_text_file'
            ),
            UrlMap(
                name='save-new-entry',
                url='hs-modflow/save-new-entry',
                controller='hs_modflow.ajax_controllers.save_new_entry'
            ),
        )

        return url_maps

    def persistent_store_settings(self):
        """
        Define Persistent Store Settings.
        """
        ps_settings = (
            PersistentStoreDatabaseSetting(
                name='primary_db',
                description='primary database',
                initializer='hs_modflow.model.init_primary_db',
                required=True
            ),
        )

        return ps_settings
