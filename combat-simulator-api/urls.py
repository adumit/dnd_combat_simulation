"""combat-simulator-api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from actors.views import get_combatants, create_combatant, load_combatant, \
    import_combatant_from_ddb
from actions.views import get_all_actions, get_all_damage_types, \
    create_action, get_all_aoe_types
from effects.views import get_all_effects, create_effect, get_all_effect_types
from simulation.views import get_simulation_results, save_battle, load_battle
from .views import FrontendAppView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('combatants', get_combatants),
    path('simulate', get_simulation_results),
    path('actions', get_all_actions),
    path('effects', get_all_effects),
    path('effectTypes', get_all_effect_types),
    path('createAction', create_action),
    path('damageTypes', get_all_damage_types),
    path('aoeTypes', get_all_aoe_types),
    path('createCombatant', create_combatant),
    path('ddbImport', import_combatant_from_ddb),
    path('loadCombatant/<str:combatant_name>/', load_combatant),
    path('createEffect', create_effect),
    path('saveBattle', save_battle),
    path('loadBattle', load_battle),
    url(r'^', FrontendAppView.as_view())
]
