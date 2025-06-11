from fastapi import FastAPI, HTTPException
import redis

app = FastAPI()

def connect_to_redis(host='localhost', port=6379, db=0):
    """Establishes a connection to the Redis server."""
    try:
        r = redis.Redis(host=host, port=port, db=db, decode_responses=True)
        # Test the connection
        r.ping()
        print(f"Successfully connected to Redis at {host}:{port}")
        return r
    except redis.exceptions.ConnectionError as e:
        print(f"Could not connect to Redis: {e}")
        return None

def publish_message(redis_client, channel, message):
    """Publishes a message to a specified Redis channel."""
    if redis_client:
        try:
            # publish returns the number of clients that received the message
            num_subscribers = redis_client.publish(channel, message)
            return(f"Published '{message}' to channel '{channel}'. Received by {num_subscribers} subscribers.")
        except redis.exceptions.RedisError as e:
            return(f"Error publishing message: {e}")
    else:
        return("Redis client not connected. Cannot publish.")

@app.post("/")
def publish(message: str):
    r_client = connect_to_redis()

    if r_client:
        my_channel = "my_channel"
        return publish_message(r_client, my_channel, message)