from ticketing_system.domain.ticket import Ticket as TicketDomain
from ticketing_system.app import db
from .models import Ticket


class TicketRepo:

    @staticmethod
    def __create_ticket_objects(results):
        return [
            TicketDomain(
                user=i.user,
                subject=i.subject,
                department=i.department,
                priority=i.priority,
                code=i.code,
                message=i.message,
                created_at=i.created_at,
                updated_at=i.updated_at,
                closed=i.closed
            )
            for i in results
        ]

    def list(self, filters=None):
        if filters:
            return self.__create_ticket_objects(
                Ticket.query.filter_by(**filters).order_by(Ticket.created_at.desc())
            )
        return self.__create_ticket_objects(Ticket.query.order_by(Ticket.created_at.desc()).all())

    def get(self, filters):
        ticket = Ticket.query.filter_by(**filters).first()
        if not ticket:
            return None
        return ticket

    def create(self, data):
        ticket = Ticket(**data)
        db.session.add(ticket)
        db.session.commit()
        return TicketDomain(
            user=ticket.user,
            subject=ticket.subject,
            department=ticket.department,
            priority=ticket.priority,
            code=ticket.code,
            message=ticket.message,
            created_at=ticket.created_at,
            updated_at=ticket.updated_at,
            closed=ticket.closed
        )

    def update(self, data):
        closed = data.pop('closed')
        ticket = Ticket.query.filter_by(**data).first()

        if not ticket:
            return None
        ticket.closed = closed
        db.session.commit()

        return TicketDomain(
            user=ticket.user,
            subject=ticket.subject,
            department=ticket.department,
            priority=ticket.priority,
            code=ticket.code,
            message=ticket.message,
            created_at=ticket.created_at,
            updated_at=ticket.updated_at,
            closed=ticket.closed
        )
