"""Namespace"""
import collections
import re

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, CheckConstraint, column, or_, and_
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import relationship, object_session

from mxdesign.entities.base import Base

name_pattern = re.compile(r'[_A-Za-z][_A-Za-z0-9]*')


class Namespace(Base):
    """Namespace"""
    __tablename__ = 'namespace'

    id = Column(Integer, primary_key=True)
    experiment_id = Column(Integer, ForeignKey('experiment.id'), nullable=True)
    parent_id = Column(Integer, ForeignKey('namespace.id'), nullable=True)
    name = Column(String(64), nullable=True)
    label = Column(String(128), nullable=True)

    experiment = relationship('Experiment', back_populates='_namespace')
    parent = relationship('Namespace', remote_side=[id], backref='children')
    variables = relationship('Variable', back_populates='namespace', cascade='all, delete-orphan')

    __table_args__ = (
        UniqueConstraint('experiment_id', 'parent_id', 'name'),
        CheckConstraint(column('name').regexp_match('^[_A-Za-z][_A-Za-z0-9]*$')),
        # belongs to an experiment or parent namespace
        CheckConstraint(or_(
            and_(column('parent_id').is_(None),
                 column('name').is_(None),
                 column('experiment_id').isnot(None)),
            and_(column('experiment_id').is_(None),
                 column('name').isnot(None),
                 column('parent_id').isnot(None)),
        )),
    )

    def __getitem__(self, item):
        """Gets/creates namespace indicated in path provided.

        Parameters
        ----------
        item: str or tuple[str] or 'Namespace'
            The path to the namespace.
        Returns
        -------
        namespace: Namespace
            The namespace at the provided path.
        """
        if isinstance(item, Namespace):
            return item
        return self.get_or_create(path=item)

    @staticmethod
    def _parse(path):
        """Parses the path to the namespace.

        Parameters
        ----------
        path: str or tuple of str
            The path to the namespace.
        Returns
        -------
        parsed_path: tuple of str
            The parsed path as tuple of strings.
        """
        parsed_path = path
        if parsed_path is None:
            parsed_path = tuple()
        elif isinstance(parsed_path, str):
            parsed_path = tuple(parsed_path.split('.'))

        if not isinstance(parsed_path, collections.Sequence) or not all(isinstance(p, str) for p in parsed_path):
            raise TypeError('expected str, tuple, found {}'.format(type(path).__name__))
        if len(parsed_path) < 1:
            return None, []
        return parsed_path[0], parsed_path[1:]

    def get(self, path):
        """Recursively get the namespace of the provided path.

        Parameters
        ----------
        path: str
            The path to get the namespace.
        Returns
        -------
        result: 'Namespace'
            The namespace for the path provided.
        """
        session = object_session(self)
        name, namepath = self._parse(path)
        if name is not None:
            result = session.query(Namespace) \
                .filter(Namespace.parent_id == self.id) \
                .filter(Namespace.name == name) \
                .one()
        else:
            result = self
        if len(namepath) == 0:
            return result
        return result.get(namepath)

    def get_or_create(self, path):
        """Recursively get/create namespace by following the provided path.

        Parameters
        ----------
        path: str or tuple[str]
            The path to follow.
        Returns
        -------
        namespace: 'Namespace'
            The namespace after following the provided path.
        """
        session = object_session(self)
        name, namepath = self._parse(path)
        if name is not None:
            try:
                result = session.query(Namespace) \
                    .filter(Namespace.parent_id == self.id) \
                    .filter(Namespace.name == name) \
                    .one()
            except NoResultFound as ex:
                result = Namespace(parent_id=self.id, name=name)
                session.add(result)
                session.commit()
        else:
            result = self
        if len(namepath) == 0:
            return result
        return result.get_or_create(namepath)

    def __repr__(self):
        return 'Namespace(id={}, name={}, path={})'.format(
            self.id, self.name, str(self)
        )

    def __str__(self):
        """Joins the path to variable from the root namespace.

        Returns
        -------
        path: str
            The full path to the namespace.
        """
        parent_path = ''
        if self.parent is not None:
            parent_path = str(self.parent)
        if self.name is None:
            return ''
        if len(parent_path) == 0:
            return self.name
        return '{}.{}'.format(parent_path, self.name)
