from django.urls import path
from .views import (account, funds, edit_funds, 
                    delete_funds, new_funds, myfunds, 
                    history, notifications, notify_back, 
                    notify, new_notify, accounts)

urlpatterns = [
    path('account', account, name='account'),
    path('funds/<int:pk>', funds, name='funds'),
    path('funds/<int:pk>/edit', edit_funds, name='edit_funds'),
    path('funds/<int:pk>/delete', delete_funds, name='delete_funds'),
    path('funds/new', new_funds, name='new_funds'),
    path('funds', myfunds, name='myfunds'),
    path('history', history, name='history'),
    path('notifications', notifications, name='notifications'),
    path('notify_back', notify_back, name='notify_back'),
    # Json response
    path('notify', notify, name='notify'),
    path('new_notify', new_notify, name='new_notify'),
    path('accounts', accounts, name='accounts')
]
