# --- Get Item in Sharepoint list
import numpy as np
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext

sp_client_id = '52fdd257-fd3e-4f56-86ca-3d5c7091c110'
sp_client_secret = 'z+pRoP0UCRZBggLALjJ2Yw/GsBo8tuZF0A4qbKK3XaI='
sp_client_credentials = ClientCredential(sp_client_id, sp_client_secret)
sp_site_url = 'https://viendaukhivn.sharepoint.com/sites/VPIDataAnalytics30RefreshPassword'
ctx = ClientContext(sp_site_url).with_credentials(sp_client_credentials)
target_list = ctx.web.lists.get_by_title("password_storage")
target_item = target_list.get_item_by_id("1")


# --- Get current_password
ctx.load(target_item)
ctx.execute_query()
item_value = target_item.properties
password = str(item_value["current_password"])

print(password)