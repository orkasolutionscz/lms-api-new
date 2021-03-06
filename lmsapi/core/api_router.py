from rest_framework.routers import DefaultRouter
from api_rbbackup.views import RouterViewSet, RouterTypeViewSet
from api_user.views import UserViewSet
from api_nodes.views import NodeViewSet, MacsViewSet, IpHistoryViewSet
from api_cash.views import CashViewSet
from api_customer.views import CustomersViewSet, CustomerBlockedViewSet, CustomerExecutedViewSet, AssignmentsViewSet
from api_netdevice.views import DevicesViewSet


router = DefaultRouter()
# Router Backup Devices
router.register('routers', RouterViewSet)
router.register('routers_type', RouterTypeViewSet)
# LMS Useri
router.register('lmsusers', UserViewSet)
router.register('nodes', NodeViewSet)
router.register('nodes_mac', MacsViewSet)
router.register('ip_history', IpHistoryViewSet)
router.register('cash_bank', CashViewSet)
router.register('customers', CustomersViewSet, basename='all')
router.register('cust_blocked', CustomerBlockedViewSet, basename='blocked')
router.register('cust_executed', CustomerExecutedViewSet, basename='executed')
router.register('cust_assigments', AssignmentsViewSet)
router.register('devices', DevicesViewSet)

