from tethys_sdk.base import TethysAppBase, url_map_maker


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
    description = 'runs modflow modflow models that are stored in hydroshare'
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
        )

        return url_maps
