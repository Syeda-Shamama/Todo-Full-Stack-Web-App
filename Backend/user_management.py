import uuid
from sqlmodel import Session, select
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from db import engine, create_db_and_tables
from models import User

def create_user(email: str, name: str, password: str):
    """Create a new user in the database"""
    # Create tables if they don't exist
    create_db_and_tables()
    
    # Create session using engine directly
    session = Session(engine)
    
    try:
        # Check if user already exists
        existing_user = session.exec(select(User).where(User.email == email)).first()
        if existing_user:
            print(f"❌ User with email {email} already exists.")
            return
        
        # Create new user
        user = User(
            id=str(uuid.uuid4()),
            email=email,
            name=name,
            password=""  # Will be set by set_password()
        )
        user.set_password(password)
        
        # Save to database
        session.add(user)
        session.commit()
        session.refresh(user)  # Get updated user with auto-generated fields
        
        print(f"✅ User '{name}' created successfully!")
        print(f"   Email: {email}")
        print(f"   ID: {user.id}")
        
    except Exception as e:
        session.rollback()
        print(f"❌ Error creating user: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Create a new user for testing.")
    parser.add_argument("email", type=str, help="User's email")
    parser.add_argument("name", type=str, help="User's name")
    parser.add_argument("password", type=str, help="User's password")
    
    args = parser.parse_args()
    
    create_user(args.email, args.name, args.password)