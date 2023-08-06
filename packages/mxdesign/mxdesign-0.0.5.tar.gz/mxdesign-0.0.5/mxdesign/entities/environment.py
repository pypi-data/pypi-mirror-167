"""Environment"""
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy.orm import sessionmaker

from mxdesign.entities.experiment import Experiment
from mxdesign.entities.base import Base


class Environment(object):
    """Environment"""

    def __init__(self, path='sqlite:///logs.db', verbose=False):
        """Creates an environment.

        Parameters
        ----------
        path: str
            The path to the environment.
        verbose: bool
            Whether to show the db logs or not.
        """
        self._path = path
        self._verbose = verbose
        self._engine = self.engine
        self._session = self.session
        self.setup()

    def setup(self):
        """Sets up the database to store the logging data.

        Returns
        -------
        self: Environment
            The current environment object.
        """
        Base.metadata.create_all(self.engine)
        return self

    @property
    def engine(self):
        """Creates or gets the engine.

        Returns
        -------
        engine: Engine
            The created database engine.
        """
        if hasattr(self, '_engine'):
            return self._engine
        return create_engine(self._path, echo=self._verbose)

    @property
    def session(self):
        """Creates/gets the session for the context.

        Returns
        -------
        session: Session
            The session object.
        """
        if hasattr(self, '_session'):
            return self._session
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def get_experiment(self, name):
        """Gets/creates an experiment from database.

        Parameters
        ----------
        name: str
            The name of experiment.
        Returns
        -------
        expr: Experiment
            Created experiment.
        """
        session = self.session
        try:
            expr = session.query(Experiment) \
                .filter(Experiment.name == name) \
                .one()
        except NoResultFound as ex:
            try:
                expr = Experiment(name=name)
                session.add(expr)
                session.commit()
            except IntegrityError as ex:
                raise ValueError('expected a alphanumeric value for name, found {}'.format(name))
        return expr
