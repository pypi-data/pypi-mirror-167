from typing import List
from uuid import UUID

from hrthy_core.security.exceptions import MissingPermissionException, MissingScopeConfiguration
from hrthy_core.security.scopes_hierarchy import HIERARCHY_SCOPES
from hrthy_core.security.security import Requester
from hrthy_core.security.types import ScopeType


class ScopeChecker:
    @staticmethod
    def has_all_permissions(requester: Requester, scopes: List[str]):
        return all(s in requester.scopes for s in scopes)

    @staticmethod
    def has_at_least_one_permission(requester: Requester, scopes: List[str]):
        return any(s in requester.scopes for s in scopes)

    @staticmethod
    def get_target_company(self, requester: Requester, scope: str, company_id: UUID = None) -> UUID:
        scope_configuration = HIERARCHY_SCOPES.get(scope, None)
        if not scope_configuration:
            raise MissingScopeConfiguration()
        if scope_configuration.get('type') != ScopeType.GLOBAL and company_id != requester.company_id:
            raise MissingPermissionException()
        return company_id if company_id is not None else requester.company_id
