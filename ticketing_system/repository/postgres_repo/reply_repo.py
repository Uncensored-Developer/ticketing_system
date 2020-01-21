from ticketing_system.domain.reply import Reply as ReplyDomain
from ticketing_system.app import db
from .models import Reply


class ReplyRepo:

    @staticmethod
    def __create_reply_objects(results):
        return [
            ReplyDomain(
                user=reply.user,
                ticket=reply.ticket,
                message=reply.message,
                created_at=reply.created_at
            )
            for reply in results
        ]

    def create(self, data):
        reply = Reply(**data)
        db.session.add(reply)
        db.session.commit()
        return ReplyDomain(
                user=reply.user,
                ticket=reply.ticket,
                message=reply.message,
                created_at=reply.created_at
            )

    def list(self, filters):
        return self.__create_reply_objects(Reply.query.filter_by(**filters).order_by(Reply.created_at.desc()))
