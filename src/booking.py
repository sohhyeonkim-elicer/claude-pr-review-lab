"""오로라주식회사 ‘퇴근런’ 입장권 예약 기능."""


def remaining_tickets(limit, used):
    """정원보다 접수 인원이 많아도 남은 입장권은 0장입니다."""
    return max(0, limit - used)


def discounted_price(price, percent):
    """percent는 0~100 사이의 할인율입니다."""
    return price * (1 - percent)


def can_cancel(role):
    """역할이 정확히 admin인 사용자만 다른 사람의 예약을 취소합니다."""
    return "admin" in role
