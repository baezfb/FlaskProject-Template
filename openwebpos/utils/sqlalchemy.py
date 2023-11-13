from flask_login import current_user
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.inspection import inspect

from openwebpos.app.extensions import db
from openwebpos.utils import timezone_datetime, gen_uuid


class CRUDMixin:
    """
    Mixin that adds convenience methods for CRUD (create, read, update, delete).
    """

    def save(self):
        """
        Saves the instance to the database.

        This method adds the instance to the database session and commits the changes.
        It does not return anything.

        :return: None
        """
        db.session.add(self)
        return db.session.commit()

    @classmethod
    def create(cls, **kwargs):
        """
        Create a new instance of the class.

        Args:
            **kwargs: keyword arguments containing the attributes of the instance

        Returns:
            The created instance.

        Raises:
            ProgrammingError: If there is an error in the execution of the SQL query.
        """
        instance = cls(**kwargs)
        try:
            instance.save()
        except ProgrammingError:
            db.session.rollback()
            raise
        return instance

    def update(self, **kwargs):
        """
        Update specific fields of a record.
        Args:
            **kwargs: Arbitrary keyword arguments.
        Returns:
            object: Updated record.
        """
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save()

    def delete(self):
        """
        Remove the record from the database.
        Returns:
            object: Deleted record.
        """
        db.session.delete(self)
        return db.session.commit()


class TrackMixin(object):
    """
    Mixin that adds created_by and updated_by columns to model
    """

    created_by = db.Column(db.String(40), nullable=True, default="system")
    updated_by = db.Column(db.String(40), nullable=True, default="system")
    created_at = db.Column(db.DateTime, default=timezone_datetime)
    updated_at = db.Column(
        db.DateTime, default=timezone_datetime, onupdate=timezone_datetime
    )

    def __init__(self, **kwargs):
        super(TrackMixin, self).__init__(**kwargs)
        if current_user.is_anonymous:
            self.created_by = "system"
            self.updated_by = "system"
        else:
            self.created_by = kwargs.get("created_by") or current_user.id
            self.updated_by = kwargs.get("updated_by") or current_user.id


class Model(CRUDMixin, TrackMixin, db.Model):
    """
    Base model class that includes CRUD convenience methods.
    """

    __abstract__ = True

    id = db.Column(
        db.String(255), primary_key=True, unique=True, nullable=False, default=gen_uuid
    )

    @classmethod
    def toggle_column(cls, column, cls_id):
        """
        Toggles the value of a column for a given instance of the class.

        Args:
            column: A string representing the name of the column to toggle.
            cls_id: The primary key value of the instance of the class to update.

        Raises:
            ProgrammingError: If an error occurs during the database session commit.

        Returns:
            None
        """
        obj = cls.query.get(cls_id)
        setattr(obj, column, not getattr(obj, column))
        db.session.commit()

    @classmethod
    def get(cls, column, cls_id):
        """
        Gets the value of a column for a given instance of the class.

        Args:
            column: A string representing the name of the column to get.
            cls_id: The primary key value of the instance of the class to get.

        Returns:
            The value of the column for the instance of the class.
        """
        obj = cls.query.get(cls_id)
        return getattr(obj, column)

    @classmethod
    def get_all(cls):
        """
        Gets all the instances of the class.

        Returns:
            A list of all the instances of the class.
        """
        return cls.query.all()

    @classmethod
    def get_by_id(cls, cls_id):
        """
        Gets an instance of the class by its primary key.

        Args:
            cls_id: The primary key value of the instance of the class to get.

        Returns:
            The instance of the class with the given primary key.
        """
        return cls.query.get(cls_id)

    @classmethod
    def get_by_name(cls, name):
        """
        Gets an instance of the class by its name.
        """
        return cls.query.filter_by(name=name).first()

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)
        if field_exists(self.__class__, "name"):
            self.name = kwargs.get("name").lower()


def foreign_key(tablename, nullable=False, pk_name="id", **kwargs):
    """
    Args:
        tablename: A string representing the name of the referenced table.
        nullable: A boolean indicating if the foreign key column allows null values. Defaults to False.
        pk_name: A string representing the name of the primary key column in the referenced table. Defaults to 'id'.
        **kwargs: Additional keyword arguments to be passed to the SQLAlchemy ForeignKey constructor.

    Returns:
        A SQLAlchemy Column object representing a foreign key column.

    """
    return db.Column(
        db.ForeignKey(f"{tablename}.{pk_name}", **kwargs), nullable=nullable
    )


def field_exists(model_class, field_name: str) -> bool:
    """
    Checks if a field exists in a given model.

    Args:
        model_class: The class of the model to check the field existence in.
        field_name (str): The name of the field to check.

    Returns:
        bool: True if the field exists in the model's columns, False otherwise.

    Raises:
        ValueError: If the `model_class` is not a subclass of `MyModel`.

    """
    if not issubclass(model_class, Model):
        raise ValueError(f"{model_class} must be a subclass of MyModel")

    inspector = inspect(model_class)

    return field_name in inspector.columns


def check_data_existence(table, field_name, data):
    """
    Checks if data exists in a specified table and field.

    Args:
        table: The table to query for data existence.
        field_name: The name of the field to query.
        data: The data to check existence for.

    Returns:
        True if the data exists in the specified table and field, False otherwise.
        If there is an error during the check, returns a string with an error message.
    """

    if field_name == "name":
        data = data.lower()

    try:
        # Query the table for the field
        result = (
            db.session.query(table).filter(getattr(table, field_name) == data).first()
        )

        # If result is not None, data exists else it does not
        return result is not None
    except ProgrammingError:
        return "Incorrect table or field"

    except Exception as e:
        return f"An unknown error occurred: {str(e)}"
