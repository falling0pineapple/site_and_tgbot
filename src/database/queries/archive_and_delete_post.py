from database.engine import session_factory
from database.models import SuggestedPostArchiveORM, SuggestedPostORM



def delete_and_archive_post(post_id: int, in_chanel: bool):
    with session_factory() as session:
        post = session.get(SuggestedPostORM, post_id)
        if post is None:
            return "None"
        session.add(SuggestedPostArchiveORM(
            post_id=post.post_id,
            title=post.title, 
            author=post.author,
            in_chanel=in_chanel
                    )
                    )
        session.delete(post)
        session.commit()
        return "deleted and archived"
        