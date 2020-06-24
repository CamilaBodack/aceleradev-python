from api.models import User, Agent, Event, Group
from datetime import date, timedelta
from django.db.models import Q


def get_active_users() -> User:
    """
    Traga todos os usuários ativos, seu último login deve ser menor que 10 dias
    """
    in_between_date = date.today() - timedelta(days=10)
    queryset = User.objects.filter(last_login__gt=in_between_date)
    return queryset


def get_amount_users() -> User:
    """Retorne a quantidade total de usuarios do sistema """
    queryset_all_user = User.objects.all()
    return len(queryset_all_user)


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    raise NotImplementedError


def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    raise NotImplementedError


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um usuário específico"""
    raise NotImplementedError


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário pelo nome do usuário"""
    raise NotImplementedError


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information"""
    raise NotImplementedError
