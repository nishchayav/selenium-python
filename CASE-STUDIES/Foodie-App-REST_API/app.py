from flask import Flask
from restaurant import restaurant_bp
from dish import dish_bp
from user import user_bp
from order import order_bp
from admin import admin_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(dish_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(admin_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
