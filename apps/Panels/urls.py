from django.urls import path
from .views import *

urlpatterns = [
    path('', ListPanelView.as_view(), name='listPanels'),
    path('SectionalPanels/', ListSectionalPanelView.as_view(), name='listSectionalPanels'),
    path('SectionalPanels/<int:business_id>', ListFilteredSectionalPanelView.as_view(), name='listFilteredSectionalPanels'),
    path('SectionalPanels/new/', CreateSectionalPanelView.as_view(), name='createSectionalPanel'),
    path('SectionalPanels/Update/<int:pk>', UpdateSectionalPanelView.as_view(), name='updateSectionalPanel'),
    path('PrincipalPanels/', ListPrincipalPanelView.as_view(), name='listPrincipalPanels'),
    path('PrincipalPanels/<int:business_id>', ListFilteredPrincipalPanelView.as_view(), name='listFilteredPrincipalPanels'),
    path('PrincipalPanels/new/', CreatePrincipalPanelView.as_view(), name='createPrincipalPanel'),
    path('PrincipalPanels/Update/<int:pk>', UpdatePrincipalPanelView.as_view(), name='updatePrincipalPanel'),
]