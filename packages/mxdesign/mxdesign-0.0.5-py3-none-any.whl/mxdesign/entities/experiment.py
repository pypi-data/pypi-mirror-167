"""Experiment"""
from sqlalchemy import Column, Integer, String, UniqueConstraint, CheckConstraint, column
from sqlalchemy.orm import relationship, object_session

from mxdesign.entities.base import Base
from mxdesign.entities.trial import Trial
from mxdesign.entities.namespace import Namespace


class Experiment(Base):
    """Experiment"""
    __tablename__ = 'experiment'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)

    _namespace = relationship('Namespace', back_populates='experiment', uselist=False, cascade='all, delete-orphan')
    trials = relationship('Trial', back_populates='experiment', cascade='all, delete-orphan')

    __table_args__ = (
        UniqueConstraint('name'),
        CheckConstraint(column('name').regexp_match('^[_A-Za-z][_A-Za-z0-9]*$')),
    )

    @property
    def namespace(self):
        """Gets the namespace of the experiment.

        If the namespace is None, it will be created and added.

        Returns
        -------
        namespace: 'Namespace'
            Namespace associated with this experiment.
        """
        session = object_session(self)
        if self._namespace is None:
            namespace = Namespace(experiment_id=self.id)
            session.add(namespace)
            session.commit()
        return self._namespace

    @property
    def ns(self):
        """Returns namespace.

        Returns
        -------
        namespace: 'Namespace'
            Same as self.namespace.
        """
        return self.namespace

    def create_trial(self):
        """Create a trial.

        Returns
        -------
        trial: Trial
            trial.
        """
        session = object_session(self)
        trial = Trial(experiment_id=self.id)
        session.add(trial)
        session.commit()
        return trial

    def __repr__(self):
        return 'Experiment(id={}, name={})'.format(
            self.id, self.name
        )
