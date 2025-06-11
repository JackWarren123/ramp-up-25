# import redis
#
# def connect_to_redis(host='localhost', port=6379, db=0):
#     """Establishes a connection to the Redis server."""
#     try:
#         r = redis.Redis(host=host, port=port, db=db, decode_responses=True)
#         # Test the connection
#         r.ping()
#         print(f"Successfully connected to Redis at {host}:{port}")
#         return r
#     except redis.exceptions.ConnectionError as e:
#         print(f"Could not connect to Redis: {e}")
#         return None
#
# def print_published_messages(redis_client):
#

import redis
import time # We'll use this for a small delay in case we need it

# --- Configuration ---
REDIS_HOST = 'localhost' # Your Redis server's address
REDIS_PORT = 6379        # Default Redis port
REDIS_CHANNEL = 'my_channel' # The channel to subscribe to (must match publisher)

def run_subscriber():
    print(f"Connecting to Redis at {REDIS_HOST}:{REDIS_PORT}...")
    try:
        # Establish a connection to Redis
        # decode_responses=True ensures messages are returned as strings, not bytes
        r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)
        print("Successfully connected to Redis.")

        # Create a PubSub object
        # This object allows us to subscribe to channels
        pubsub = r.pubsub()

        # Subscribe to the specified channel
        pubsub.subscribe(REDIS_CHANNEL)
        print(f"Subscribed to channel: '{REDIS_CHANNEL}'")
        print("Waiting for messages... (Press Ctrl+C to exit)")

        # Start listening for messages
        # The .listen() method yields messages as they arrive
        for message in pubsub.listen():
            # The 'listen' method returns different types of messages:
            # - 'subscribe' messages when you successfully subscribe
            # - 'message' messages when data is published to the channel
            if message['type'] == 'message':
                channel = message['channel']
                data = message['data']
                print(f"[{channel}] Received message: {data}")
            # Optional: You can print other message types for debugging
            # else:
            #     print(f"Received non-message type: {message}")

    except redis.exceptions.ConnectionError as e:
        print(f"Error connecting to Redis: {e}")
        print("Please ensure your Redis service is running.")
    except KeyboardInterrupt:
        print("\nSubscriber stopped by user.")
    finally:
        # Clean up: close the connection (optional, as the script exits)
        if 'pubsub' in locals() and pubsub:
            pubsub.unsubscribe(REDIS_CHANNEL)
            print(f"Unsubscribed from channel: '{REDIS_CHANNEL}'")
        if 'r' in locals() and r:
            r.close()
            print("Redis connection closed.")

if __name__ == "__main__":
    run_subscriber()