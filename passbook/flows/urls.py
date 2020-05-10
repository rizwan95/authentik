"""flow urls"""
from django.urls import path

from passbook.flows.models import FlowDesignation
from passbook.flows.views import (
    FlowExecutorView,
    FlowPermissionDeniedView,
    ToDefaultFlow,
)

urlpatterns = [
    path("-/denied/", FlowPermissionDeniedView.as_view(), name="denied"),
    path(
        "-/default/auth/",
        ToDefaultFlow.as_view(designation=FlowDesignation.AUTHENTICATION),
        name="default-auth",
    ),
    path(
        "-/default/recovery/",
        ToDefaultFlow.as_view(designation=FlowDesignation.RECOVERY),
        name="default-recovery",
    ),
    path(
        "-/default/enrollment/",
        ToDefaultFlow.as_view(designation=FlowDesignation.ENROLLMENT),
        name="default-enrollment",
    ),
    path(
        "-/default/password_change/",
        ToDefaultFlow.as_view(designation=FlowDesignation.PASSWORD_CHANGE),
        name="default-password-change",
    ),
    path("<slug:flow_slug>/", FlowExecutorView.as_view(), name="flow-executor"),
]
