from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

from logger import Logger

_logger = Logger(__name__).get_logger()

class BlogPost(BaseModel):
    id: int
    title: str
    content: str

blog_posts = []

app = FastAPI()

@app.post("/blog/")
async def create_blog_post(post: BlogPost):
    try:
        blog_posts.append(post.model_dump())
        return {"status": "success"}, status.HTTP_201_CREATED
    except Exception as e:
        _logger.error("An exception happens on post creation: %s", str(e))
        return f"An exception popout: {str(e)}"
    
@app.get("/blog/")
async def get_blog_posts():
    try:
        return [{post.get('id'), post.get('title'), post.get('content')} for post in blog_posts]
    except Exception as e:
        _logger.error("An exception happens on post retrieval: %s", str(e))
        return f"An exception popout: {str(e)}"

@app.get("/blog/{post_id}")
async def get_blog_post(post_id: int):
    try:
        return [post for post in blog_posts if post.get('id') == post_id]
    except Exception as e:
        _logger.error("An exception happens on post retrieval: %s", str(e))
        return f"An exception popout: {str(e)}"

@app.put("/blog/{post_id}")
async def update_blog_post(post_id: int, post: BlogPost):
    try:
        post_index = [index for index, post in enumerate(blog_posts) if post.get('id') == post_id]
        blog_posts[post_index[0]] = post.model_dump()
        if not post_index:
            _logger.warning("Post with id %s not found", post_id)
            return {"status": "failed", "message": f"Post with id {post_id} not found"}, status.HTTP_404_NOT_FOUND
        return {"status": "success"}, status.HTTP_200_OK
    except Exception as e:
        _logger.error("An exception happens on post update: %s", str(e))
        return f"An exception popout: {str(e)}"

@app.delete("/blog/{post_id}")
async def delete_blog_post(post_id: int):
    try:
        post_index = [index for index, post in enumerate(blog_posts) if post.get('id') == post_id]
        blog_posts.pop(post_index[0])
        if not post_index:
            _logger.warning("Post with id %s not found", post_id)
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")
        return {"status": "success"}, status.HTTP_200_OK
    except Exception as e:
        _logger.error("An exception happens on post deletion: %s", str(e))
        return f"An exception popout: {str(e)}"