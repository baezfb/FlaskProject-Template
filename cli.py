import os
import secrets

from click_shell import shell

blueprint_path = os.path.join("openwebpos", "blueprints")
print(blueprint_path)


@shell(prompt="openwebpos-shell > ", intro="Starting openwebpos shell...")
def openwebpos():
    pass


@openwebpos.command()
def addblueprint():
    """Add a blueprint to the app"""
    blueprint_name = input("Enter the name of the blueprint: ")
    # Check if blueprint already exists
    if os.path.exists(os.path.join(blueprint_path, blueprint_name)):
        print("Blueprint already exists")
        return
    # Create blueprint folder
    os.makedirs(os.path.join(blueprint_path, blueprint_name))
    # Create __init__.py file
    with open(os.path.join(blueprint_path, blueprint_name, "__init__.py"), "w") as f:
        f.write(
            f"from flask import Blueprint\n\n{blueprint_name}_bp = Blueprint('{blueprint_name}', __name__, template_folder='templates', url_prefix='/{blueprint_name}/')\n"
        )
    # Add models folder to blueprint
    os.makedirs(os.path.join(blueprint_path, blueprint_name, "models"))
    # Create __init__.py file
    with open(
        os.path.join(blueprint_path, blueprint_name, "models", "__init__.py"), "w"
    ) as f:
        f.write("")
    # Add views folder to blueprint
    os.makedirs(os.path.join(blueprint_path, blueprint_name, "views"))
    # Create __init__.py file
    with open(
        os.path.join(blueprint_path, blueprint_name, "views", "__init__.py"), "w"
    ) as f:
        f.write("")
    # Add forms folder to blueprint
    os.makedirs(os.path.join(blueprint_path, blueprint_name, "forms"))
    # Create __init__.py file
    with open(
        os.path.join(blueprint_path, blueprint_name, "forms", "__init__.py"), "w"
    ) as f:
        f.write("")
    # Add templates folder to blueprint
    os.makedirs(
        os.path.join(blueprint_path, blueprint_name, "templates/" + blueprint_name)
    )
    with open("openwebpos/blueprints/__init__.py", "a") as f:
        f.write(f"from .{blueprint_name} import {blueprint_name}_bp\n")


@openwebpos.command()
def gensecret():
    """Generate a secret key"""
    print(secrets.token_hex())


if __name__ == "__main__":
    openwebpos()
